pca\_main module
================

.. automodule:: pca_main
   :members:
   :undoc-members:
   :show-inheritance:

.. code-block:: python

  self.list_patient_names=list(np.arange(len(self.list_patient)))

creating ID for patient

.. code-block:: python

  self.list_attributes=self.list_patient[0].get_Attributes()

Getting attributes from a patient object

.. code-block:: python

  self.plot_traits = list([self.plt_0.subplot2grid((2, 5), (0, 0)), self.plt_0.subplot2grid((2, 5), (0, 1)),
                            self.plt_0.subplot2grid((2, 5), (0, 2)), self.plt_0.subplot2grid((2, 5), (0, 3)),
                            self.plt_0.subplot2grid((2, 5), (0, 4))])

creatng list of  plot objects

.. code-block:: python

  for x in self.list_patient:
      self.X.append(x.get_Values())

Accessing the values and appending this to the created list

.. code-block:: python

  self.X_transp = np.transpose(self.X)

Transposing the vector

.. code-block:: python

  self.X_meaned = self.X - self.np_0.mean(self.X, axis=0)
  self.cov_mat = self.np_0.cov(self.X_meaned, rowvar=False)
  eigen_values, eigen_vectors = self.np_0.linalg.eigh(self.cov_mat)
  sorted_index = self.np_0.argsort(eigen_values)[::-1]
  self.sorted_eigenvalue = eigen_values[sorted_index]
  self.sorted_eigenvectors = eigen_vectors[:, sorted_index]

This is the Computational part. Here the meancentering of the data is done,
then the matrix Covariance and eigen values are calculated

.. code-block:: python

  self.X_reduced_transp = np.transpose(self.X_reduced)

This is the final reduced Vector
