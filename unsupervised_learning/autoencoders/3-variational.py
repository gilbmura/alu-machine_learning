#!/usr/bin/env python3
"""Create a variational autoencoder."""

import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims):
    """Build and return the encoder, decoder, and compiled autoencoder.

    Args:
        input_dims: Number of input features.
        hidden_layers: Widths of the encoder's hidden layers.
        latent_dims: Number of latent features.

    The encoder returns the latent sample, mean, and log variance.
    The decoder reverses the encoder's hidden layer widths.
    Training uses Adam with binary cross-entropy and KL divergence.
    """
    inputs = keras.Input(shape=(input_dims,))
    encoded = inputs
    for units in hidden_layers:
        encoded = keras.layers.Dense(units, activation='relu')(encoded)

    z_mean = keras.layers.Dense(latent_dims, activation=None)(encoded)
    z_log_var = keras.layers.Dense(latent_dims, activation=None)(encoded)

    def sampling(args):
        """Sample a latent vector using the reparameterization trick."""
        mean, log_var = args
        epsilon = keras.backend.random_normal(
            shape=keras.backend.shape(mean))
        return mean + keras.backend.exp(0.5 * log_var) * epsilon

    z = keras.layers.Lambda(sampling, output_shape=(latent_dims,))(
        [z_mean, z_log_var])
    encoder = keras.Model(inputs, [z, z_mean, z_log_var])

    decoder_inputs = keras.Input(shape=(latent_dims,))
    decoded = decoder_inputs
    for units in reversed(hidden_layers):
        decoded = keras.layers.Dense(units, activation='relu')(decoded)
    outputs = keras.layers.Dense(input_dims, activation='sigmoid')(decoded)
    decoder = keras.Model(decoder_inputs, outputs)

    auto = keras.Model(inputs, decoder(z))

    def vae_loss(x, reconstruction):
        """Combine reconstruction error and latent KL divergence."""
        reconstruction_loss = keras.backend.binary_crossentropy(
            x, reconstruction)
        reconstruction_loss = keras.backend.sum(
            reconstruction_loss, axis=-1)
        kl_loss = -0.5 * keras.backend.sum(
            1 + z_log_var - keras.backend.square(z_mean)
            - keras.backend.exp(z_log_var), axis=-1)
        return reconstruction_loss + kl_loss

    auto.compile(optimizer='adam', loss=vae_loss)
    return encoder, decoder, auto
