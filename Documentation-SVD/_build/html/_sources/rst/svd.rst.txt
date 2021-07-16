svd module
==========

.. automodule:: svd
   :members:
   :undoc-members:
   :show-inheritance:

.. code-block:: python

  u,sigma,v=np.linalg.svd(A)
  SIGMA=np.diag(sigma)

SVD decomposition using numpy

.. code-block:: python

  trans_xygrid=np.matmul(u , self.xygrid)
  trans_xygrid=np.matmul(SIGMA,self.xygrid)
  trans_xygrid=np.matmul(v,self.xygrid)

Both rotations and scaling is applied on the grid space
