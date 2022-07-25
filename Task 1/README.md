# Task 1 Overview (Copied from Forage: Lyft Program):
Lyft is in the process of rolling out a new rental fleet in the hopes of encouraging more connected, sustainable cities across the US. 

You are the fortunate inheritor of an unfortunately messy component utilized by the rental fleet’s new logistics system. 
The component is responsible for determining whether cars in Lyft’s new rental fleet should be serviced when they are returned.
Whether or not a car should be serviced depends on two factors at the moment - the engine and battery. 
There are five car models in Lyft’s fleet, each with a different engine-battery combination. 
Each of the three types of engines has its own criteria for determining when it should be serviced.
The same applies to each type of battery. These service criteria will change somewhat frequently in the future, and new car models are bound to be added to the fleet. 


With this in mind, it’s very important that the component is extensible and easy to modify, so new service criteria can be added quickly and efficiently.
Just today, you learned that the system must also take tires into account when determining if a car should be serviced in the future. 
Tacking this functionality onto the current system would be difficult and messy - instead, you have been instructed to take the time to refactor the codebase prior to making the change. 
The first step of this process is to draft up a new (clean) system architecture that will allow for the seamless inclusion of the new functionality. Your task is to draft and submit a class diagram that maps out how the system will be reorganized.

# Mission Overview:
Your plan should allow easy extensibility going forward. 
It should be trivial to add new service criteria and change which parts each car model includes (e.g. change the battery installed on the Thovex from a Nubbin to a Spindler). 
Additionally, making a change to the service criteria for a given car part should only require making a change in one place.

# Why did I choose this design pattern?
1. I have chosen to use State Behavioral Design Pattern
2. I have used it due to its ease of change of class by changing state. This means Lyft's rental cars can now change engines or batteries or tires with ease.
3. This pattern has made extensibility easier (we just have to create a new Car class and give it the State Object).
4. It is also relatively easy to add new service criteria since we just have to account for new possible combination of states.
