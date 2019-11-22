Introduction
============

Project Deliverables
--------------------

To develop a modular black-box system, complete with a sensory and controller
array targeted for fully autotomizing any e-rickshaw, especially in an Indian
road setting such that provided any destination (in the form of GPS coordinates
through an interactive interface), the vehicle should be able to navigate to
that destination completely autonomously.

Apart from being correct, the learning program should also be *empirical* in
nature - The system responsible for perception, detection, etc. should learn
from experiences over time.

Additional Objective
^^^^^^^^^^^^^^^^^^^^

An additional objective, and a challenging problem for the development team is
to package the entire device as a modular black-box model, which could then be
easily configured with any e-rickshaw.

Constraints
-----------

As discussed in the college-wide-meeting (September 5, 2019), the problem at
hand was broken down into multiple pieces and modeled with following constaints:

* Vehicle of Interest: *E-rickshaw* - These rickshaws have a M.S (Mild Steel)
  tubular Chassis, consist of 3 wheels with a differential mechanism at rear
  wheels, and are completely batter operated. The motor is brushless DC motor
  manufactured mostly in India and China. The electrical system used in Indian
  version is 48V.

  Given the interest of the ST :math:`\mu` in an autonomous battery
  operated vehicle, and the scope, but a general lack in market regarding the
  availability of this crucial piece of technology, it was decided that an
  “E-Rickshaw” shall be the only vehicle of interest.

* The GPS coordinates of the source (live) and that of the destination (static)
  shall be available at all times.

* The optimum path connecting the source with the destination is already known
  apriory.

* Aimed towards Indian market

* Speed at all times shall not exceed 20km/h.

* Maximum payload at any given time = 300 kgs.

* Maximum turn angle to be encountered anywhere along the path may not exceed
  90◦.

Software Used
-------------

The following software (all available under an open source license, unless
otherwise noted) were used. And, for the same, the authors would like to thank
the maintainers of these projects:

(Please note that this list is sorted alphabetically)

* Keras

.. raw:: latex

   \begin{itemize}
      \item \LaTeX 
   \end{itemize}

* Python
* Sphinx
* TensorFlow
* Visual Studio Code
