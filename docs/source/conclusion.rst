Conclusion
==========

The goal of this phase of the project was to extract as much information as
possible from the imagery data available at hand. Currently, we can robustly
detect the lane lines on an highway, detect and classify other vehicles (cars,
trucks, motorbikes) and with limited success, calculate distance between these
vehicles/obstacles and camera.

Limitations & Future Work
~~~~~~~~~~~~~~~~~~~~~~~~~

The current system performs very well in a highway environment, which was the
stipulated environment for this project. However, it does not generalize very
well to urban environments, which may affect the usability and accessibility of
such a system.

The system tracks a great deal of information about the environment, but there
is still a lot to be harnessed, for eg:

* Traffic Signal Detection

* Predicting behavior of other vehicles on the road.

* Analyzing Auditory Data - Is there a car honking nearby, or an emergency
  vehicle (police car/ambulance/fire-truck) siren nearby?

Also, the capability of our system to sense and analyze information is hugely
dependent on the compute power available at hand, which in favour of economic
factors, has been limited to minimal in this project.

In the phase 2 of the project, our focus shall change from gathering information
to decision making. Answering the question that "Once, we have a rich map of our
surroundings, how does a vehicle take the next decision" has to serve as the
reference for future work of the project.

Last but not the least, as we've already seen in :ref:`Moral Ethics`, developing
an autonomous vehicle may have serious implications on human life and it's worth
spending the time upon to think about the various ways in which we can protect
the privacy of people, make cars more safer and have much more rigorous legal
standards for Autonomous Vehicles.
