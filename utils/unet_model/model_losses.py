from keras import backend as K

import segmentation_models as sm

dice_loss_fun = sm.losses.DiceLoss()
bce_loss_fun = sm.losses.BinaryCELoss()
import tensorflow as tf
from typing import Union, Callable

def bce_dice_loss(y_true, y_pred):
    dice_loss = dice_loss_fun(y_true, y_pred)
    bce_loss = bce_loss_fun(y_true, y_pred)
    return 0.5 * dice_loss + 0.5 * bce_loss

#metrics
def dice_coef(y_true, y_pred, smooth=1):
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    coef = (2. * intersection + smooth) \
           / (K.sum(y_true_f) + K.sum(y_pred_f) + smooth)
    return coef


def convert_to_logits(y_pred: tf.Tensor) -> tf.Tensor:
    """
    Converting output of sigmoid to logits.
    :param y_pred: Predictions after sigmoid (<BATCH_SIZE>, shape=(None, <IMAGE_HEIGHT>, <IMAGE_WIDTH>, 1)).
    :return: Logits (tf.Tensor, shape=(<BATCH_SIZE>, <IMAGE_HEIGHT>, <IMAGE_WIDTH>, 1))
    """
    # To avoid unwanted behaviour of log operation
    y_pred = K.clip(y_pred, tf.keras.backend.epsilon(), 1 - tf.keras.backend.epsilon())

    return K.log(y_pred / (1 - y_pred))

class MyMeanIOU(tf.keras.metrics.MeanIoU):
    def update_state(self, y_true, y_pred, sample_weight=None):
        return super().update_state(tf.argmax(y_true, axis=-1), tf.argmax(y_pred, axis=-1), sample_weight)

def binary_weighted_cross_entropy(beta: float, is_logits: bool = False) -> Callable[[tf.Tensor, tf.Tensor], tf.Tensor]:
    """
    Weighted cross entropy. All positive examples get weighted by the coefficient beta:
        WCE(p, p̂) = −[β*p*log(p̂) + (1−p)*log(1−p̂)]
    To decrease the number of false negatives, set β>1. To decrease the number of false positives, set β<1.
    If last layer of network is a sigmoid function, y_pred needs to be reversed into logits before computing the
    weighted cross entropy. To do this, we're using the same method as implemented in Keras binary_crossentropy:
    https://github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/backend.py#L3525
    Used as loss function for binary image segmentation with one-hot encoded masks.
    :param beta: Weight coefficient (float)
    :param is_logits: If y_pred are logits (bool, default=False)
    :return: Weighted cross entropy loss function (Callable[[tf.Tensor, tf.Tensor], tf.Tensor])
    """
    def loss(y_true: tf.Tensor, y_pred: tf.Tensor) -> tf.Tensor:
        """
        Computes the weighted cross entropy.
        :param y_true: True masks (tf.Tensor, shape=(<BATCH_SIZE>, <IMAGE_HEIGHT>, <IMAGE_WIDTH>, 1))
        :param y_pred: Predicted masks (tf.Tensor, shape=(<BATCH_SIZE>, <IMAGE_HEIGHT>, <IMAGE_WIDTH>, 1))
        :return: Weighted cross entropy (tf.Tensor, shape=(<BATCH_SIZE>,))
        """
        if not is_logits:
            y_pred = convert_to_logits(y_pred)

        wce_loss = tf.nn.weighted_cross_entropy_with_logits(labels=y_true, logits=y_pred, pos_weight=beta)

        # Average over each data point/image in batch
        axis_to_reduce = range(1, K.ndim(wce_loss))
        wce_loss = K.mean(wce_loss, axis=axis_to_reduce)

        return wce_loss

    return loss
