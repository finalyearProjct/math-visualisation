monto module
============

.. automodule:: monto
   :members:
   :undoc-members:
   :show-inheritance:
.. code-block:: python

  ani=anim.FuncAnimation(self.figure,self.animate,interval=self.time_gap*1000)

Creating animation function according to the TIME_GAP

.. code-block:: python

  self.time_gap=time_interval

The time interval for each small circle created

.. code-block:: python

  self.radi=25

size of the large circle

.. code-block:: python

  if mag<self.radi:
    self.hit=self.hit+1
  value=self.hit*50*50/(self.total*self.np_0.square(self.radi))

Checking whether the small circle is insdie the big circle and calculating the value of pi from Area(Square),Area(Circle),Total hit,Total picks
