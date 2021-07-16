inverse\_transform module
=========================

.. automodule:: inverse_transform
   :members:
   :undoc-members:
   :show-inheritance:

.. code-block:: python

  self.ss_0=ss

This is the  statistics module,which is used for plotting the shape of normal distribution.

.. code-block:: python

  self.y_values_0=ss.norm.cdf(self.x_values,0,1)

For plotting the cumulative distribution function.

.. code-block:: python

  inverse_value=self.ss_0.norm.ppf(sample)

Mapping with the help of inverse CDF.
