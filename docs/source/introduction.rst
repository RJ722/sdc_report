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

* **Keras** is a high-level neural networks API, written in Python and
  capable of running on top of TensorFlow, CNTK, or Theano. It was developed
  with a focus on enabling fast experimentation.

.. raw:: latex

    \begin{itemize}
        \item \textbf{\LaTeX} is a high-quality typesetting system. It includes
        features designed for the production of technical and scientific
        documentation. This report was typeset and compiled using the
        \texttt{pdflatex} compiler. However, the markup was first written in
        reStructuredText, and later transpiled using \texttt{sphinx}.
    \end{itemize}


* **OpenCV** (Open Source Computer Vision Library: http://opencv.org) is
  an open-source BSD-licensed library that includes several hundreds of
  computer vision algorithms.

* **Python** is an interpreted, high-level, general-purpose programming
  language. Python's design philosophy emphasizes code readability with its
  notable use of significant whitespace.

* **Sphinx** is a tool that makes it easy to create intelligent and beautiful
  documentation for Python projects. Sphinx uses reStructuredText as its markup
  language.

* **TensorFlow** is an end-to-end open source platform for machine learning. It
  has a comprehensive, flexible ecosystem of tools, libraries and community
  resources that lets researchers push the state-of-the-art in ML and
  developers easily build and deploy ML powered applications.

* **Visual Studio Code** is a code editor redefined and optimized for building
  and debugging modern web and cloud applications. It includes support for
  debugging, embedded Git control and GitHub, syntax highlighting, intelligent
  code completion, snippets, and code refactoring.
