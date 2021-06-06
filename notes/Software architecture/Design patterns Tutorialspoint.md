---
title: Design patterns Tutorialspoint
tags: Software architecture
---

# Table of Contents
[toc]

# Design pattern Tutorialspoint
**Types of design patterns**.
* *Creational patterns*. Provide a way to create objects while hiding the creation logic, rather than instantiating objects directly using `new` operator

    $\to$ This gives program more flexibility in deciding which objects required to be created for a given use case
* *Structural patterns*. Concern class and object composition

    >**NOTE**. Concept of inheritance is used to compose interfaces and define ways to compose objects to obtain new functionality

* *Behavioral patterns*. Concern with communication between objects
* *J2EE patterns*.Concern with the presentation tier

## Creational patterns
**Factory pattern**. One of the most used design patterns
* *Idea*. 
    * Create object without exposing the creation logic to the client
    * Refer to newly created object using a common interface
* *Implementation*.

    ```java=
    public interface Shape{
        void draw();
    }
    
    public class Rectangle implements Shape{
        @Override
        public void draw(){
            System.out.println("Rectangle");
        }
    }
    
    public class Square implements Shape{
        @Override
        public void draw(){
            System.out.println("Square");
        }
    }
    
    public class ShapeFactory{
        public Shape getShape(String shapeType){
            if(shapeType.equalsIgnoreCase("Rectangle"))
                return new Rectangle();
            else if(shapeType.equalsIgnoreCase("Square"))
                return new Square();
            else return null;
        }
    }
    
    public class Demo{
        public static void main(String[] args){
            ShapeFactory shapeFactory = new ShapeFactory();
            Shape rect = shapeFactory.getShape("Rectangle");
            rect.draw();
        }
    }
    ```

* *Usage*.
    * When we need a complicated process for constructing the object, i.e.

        ```java=
        public class CarFactory{
            public Shape createCar(InputMaterial inputMaterials){
                CarWheel wheels = makeWheels(inputMaterials);
                CarCover cover = makeCover(inputMaterials);
                CarEngine engine = makeEngine(inputMaterials);
                Car car = makeCar(enginer, wheels, cover);
                return car;
            }
        }
        ```
        
    * When the construction needs a dependency, which we do not want to expose, i.e.

        ```javascript=
        class HouseFactory {
            public function create() {
                $TVObj = new TV($param1, $param2, $param3);
                $LivingroomObj = new LivingRoom($TVObj, $param1, $param2);
                $KitchenroomObj = new Kitchen($param1, $param2);
                $HouseObj = new House($LivingroomObj, $KitchenroomObj);

                return $HouseObj;
            }
        }
        ```
    
    * When we have several constructors with the same parameter type but with different behavior

**Abstract factory pattern**. One of the best ways to create an object
* *Idea*. Work around a super-factory, which create other factories
* *Implementation*.
    * *Interfaces and classes*.
    
        ```java=
        public interface Shape{
            void draw();
        }

        public class Rectangle implements Shape{
            @Override
            public void draw(){
                System.out.println("Rectangle");
            }
        }

        public class Square implements Shape{
            @Override
            public void draw(){
                System.out.println("Square");
            }
        }

        public class RoundedRectangle implements Shape{
            @Override
            public void draw(){
                System.out.println("RoundedRectangle");
            }
        }

        public class RoundedSquare implements Shape{
            @Override
            public void draw(){
                System.out.println("RoundedSquare");
            }
        }
        ```
    
    * *Factories*.
        ```java=
        public abstract class AbstractFactory{
            abstract Shape getShape(String shapeType);
        }

        public class ShapeFactory extends AbstractFactory{
            @Override
            public Shape getShape(String shapeType){
                if(shapeType.equalsIgnoreCase("Rectangle"))
                    return new Rectangle();
                else if(shapeType.equalsIgnoreCase("Square"))
                    return new Square();
                else return null;
            }
        }

        public class RoundedShapeFactory extends AbstractFactory{
            @Override
            public Shape getShape(String shapeType){
                if(shapeType.equalsIgnoreCase("RoundedRectangle"))
                    return new RoundedRectangle();
                else if(shapeType.equalsIgnoreCase("RoundedSquare"))
                    return new RoundedSquare();
                else return null;
            }
        }
        
        public class FactoryProducer{
            public static AbstractFactory getFactory(boolean rounded){
                if(rounded) 
                    return new RoundedShapeFactory();
                else
                    return new ShapeFactory();
            }
        }
        ```
    
    * *Demo*.
        ```java=
        public class Demo{
            public static void main(String[] args){
                FactoryProducer factoryProducer = new FactoryProducer();
                AbstractFactory shapeFactory = factoryProducer.getFactory(false);
                Shape rect = shapeFactory.getShape("Rectangle");
                rect.draw();
            }
        }
        ```

* *Usage*.
    * Create a collection of related products, which are designed to be used together

        <div style="text-align:center">
            <img src="/media/77fEMJB.png">
            <figcaption>Example of creating themes with abstract factory</figcaption>
        </div>
    
    * Configure a system with one of multiple families of products

        $\to$ The pattern ensures that only one of the subset of families of products will be used at any time
        * *Example*. When using abstract factory to create a theme, we can have any number of theme families made up of themed components

            $\to$ But our system should only be used with one of these at any given time
    * Make the system have independence between creation, composition, and representation of its products
        
        $\to$ The pattern provides this by decoupling the implementation of each of these operations
    * Hide implementation of our products, only revealing the required interface to provide access to their use

**Singleton pattern**. One of the simplest design patterns
* *Idea*. 
    * Create an object while making sure that only single object gets created
    * Provide a way to access its only object directly, without the needs of instantiate the object of the singleton class
* *Implementation*.
    
    ```java=
    public class SingleObject{
        private static SingleObject instance = new SingleObject();
        
        private SingleObject(){}
        
        public static SingleObject getInstance(){
            return instance;
        }
    }
    
    public class Demo{
        public static void main(String[] args){
            SingleObject object = SingleObject.getInstance();
        }
    }
    ```

* *Usage*.
    * Used for global configuration, e.g. `Database`, `LoggingManager`, etc.

        >**NOTE**. Logging is a specific example of an "acceptable" Singleton, since it does not affect the execution of our code
    
    * Used to manage a shared resource, i.e. database connection

    >**NOTE**. Be careful of using singletons to control business logic
    
* *Bad sides*.
    * Singleton objects are generally used as a global instance
    * Singleton pattern violates the single responsiblity principle
        * *Explain*. They control their own creation and lifecycle
    * They inherently cause code to be tightly coupled
    * They carry state around for the lifetime of the application

**Builder pattern**. Build a complex object using simple obejcts, and using a step-by-step approach

>**NOTE**. This builder is independent of other objects
>$\to$ This is one of the best ways to create an object

* *Idea*. Objects requiring laborious, step-by-step intialization of many fields and nested object are usually constructed inside a monstrous constructor with lots of parameters

    $\to$ We should extract the object construction code out of its own class, and move it to separate objects called *builders*

* *Implementation*.
    
    ```java=
    public class HouseBuilder{
        public House getResult(){
            House house = new House();
            house = this.buildWalls(house);
            house = this.buildDoors(house);
            house = this.buildWindows(house);
            house = this.buildRoof(house);
            return house;
        }
        
        private House buildWalls(House house){...};
        
        private House buildDoors(House house){...};
        
        private House buildWindows(House house){...};
        
        private House buildRoof(House house){...};
    }
    ```

* *Variations*.
    * We can create several different builder classes implementing the same set of building steps, but in a different manner
        
        $\to$ We can use these builders in the construction process to produce different kings of objects
    * *Director*. We can extract a series of calls to the builder steps we use to construct a product into a seprate class called *director*

        $\to$ The directory class defines the order, in which to execute the building steps, while the builder provides the implementation of the steps
        * *Pros*. 
            * Good place to put various construction routines so we can use them across our program
            * Completely hides the details of product construction from the client code, i.e. we only need to associate a builder with a directory
* *Pros and cons*.
    * *Pros*.
        * Allow us to vary a product's internal representation
        * Encapsulate code for construction and representation
        * Provide control over steps of construction process
    * *Cons*.
        * Require creating a separate `Builder` class for each product type
        * Require builder classes to be mutable
        * Dependency injection maybe less supported

**Prototype pattern**. Create duplicate object without making our code dependent on its class
* *Idea*. Implement a prototype interface, which tells to create a clone of the current object, in case directly creating a new object is costly, i.e.
    * Delegate the cloning process to the actual objects being cloned
    * Declare a common interface for all objects which support cloning

        $\to$ This interface lets us clone an object without coupling our code to the class of the object
* *Implementation*. The prototype interface contains just a single `clone` method

    * *Abstract class*. Suppose that we have implemented a class `Cloneable` having a method `clone()`

        ```java=
        public abstract class Shape implements Cloneable {

            private String id;
            protected String type;

            abstract void draw();

            public String getType(){
                return type;
            }

            public String getId() {
                return id;
            }

            public void setId(String id) {
                this.id = id;
            }

            public Object clone() {
                Object clone = null;

                try {
                    clone = super.clone();
                } catch (CloneNotSupportedException e) {
                    e.printStackTrace();
                }

                return clone;
            }
        }
        ```
    
    * *Classes*.

        ```java=
        public class Rectangle extends Shape {
            public Rectangle(){
                type = "Rectangle";
            }

            @Override
            public void draw() {
                System.out.println("Inside Rectangle::draw() method.");
            }
        }
        
        public class Square extends Shape {
            public Square(){
                type = "Square";
            }

            @Override
            public void draw() {
                System.out.println("Inside Square::draw() method.");
            }
        }
        ```
    
    * *Cache class*.

        ```java=
        import java.util.Hashtable;

        public class ShapeCache {

            private static Hashtable<String, Shape> shapeMap  = new Hashtable<String, Shape>();
            
            public static Shape getShape(String shapeId) {
                Shape cachedShape = shapeMap.get(shapeId);
                return (Shape) cachedShape.clone();
            }

            public static void loadCache() {
                Square square = new Square();
                square.setId("2");
                shapeMap.put(square.getId(),square);

                Rectangle rectangle = new Rectangle();
                rectangle.setId("3");
                shapeMap.put(rectangle.getId(), rectangle);
            }
        }
        ```
    
    * *Demo*.

        ```java=
        public class Demo {
            public static void main(String[] args) {
                ShapeCache.loadCache();
                
                Shape clonedShape2 = (Shape) ShapeCache.getShape("2");
                System.out.println("Shape : " + clonedShape2.getType());		

                Shape clonedShape3 = (Shape) ShapeCache.getShape("3");
                System.out.println("Shape : " + clonedShape3.getType());		
            }
        }
        ```
    
* *Usage*. We can create a set of objects, i.e. called `Cache`, configured in various ways

    $\to$ When we need an object like the one we have configured, we just clone a prototype, instead of constructing a new object from scratch
* *Pros*. We can copy private fields of an object, since the object supporting cloning have access to its private fields

## Structural patterns
**Adapter pattern**. A bridge between two incompatible interfaces
* *Idea*. Have a single class, which is responsible to join functionalities of independent or incompatible interfaces

**Bridge pattern**. Used when we need to decouple an abstraction from its implementation, so that the two can vary independently
* *Brief*. Have an interface, which acts as a bridge which makes the functionality of concrete class independent from interface implementer class

    $\to$ Both classes can be altered structurally without affecting each other
* *Idea*. Pick a dimension, i.e. feature or attribute, of the abstraction class, which may vary across refined abstraction classes, and abstract it

    $\to$ This is much like doing PCA on the set of possible children classes, i.e. to choose which dimensions vary much and work on those dimensions independently only

* *Illustration*.

    <div style="text-align:center">
        <img src="/media/NFE04HO.png">
        <figcaption>Illustration of bridge pattern</figcaption>
    </div>

    * *Abstraction (abstract class)*. Define the abstract interface, and maintain the Implementator reference

        $\to$ This provides high-level control logic, and relies on the implementation object to do the actual low-level work
    
    * *Refined abstraction (class)*. Extend the interface defined by Abstraction

        $\to$ Provide variants of contorl logic. Like their parent, they work with different implementations via the general implementation interface

    * *Implementator (interface)*. Define the interface for implementation classes

        $\to$ This declares the common interface for all concrete implementations
    
    * *Concrete implementator (class)*. Implement the Implementator interface

        $\to$ Contain platform-specific code
    
* *Examples*.

    <div style="text-align:center">
        <img src="/media/D9RHIcs.png">
        <figcaption>Example 1</figcaption>
    </div>

    <div style="text-align:center">
        <img src="/media/D1MFgC0.png">
        <figcaption>Example 2. We abstract the message sending method from abstract class</figcaption>
    </div>

**Filter pattern**. Also called Criteria pattern. 
* *Purpose*. Enable developers to 
    * Filter a set of object, using different criteria and
    * Chain the criteria in a decoupled way through logical operations
* *Idea*. A simple pattern of criteria pattern is
    1. Implement a set of criteria classes, each of which has method `meetCriteria`
    2. Implement `AndCriteria` and `OrCriteria` classes, acting as a combinator of any two criterias
        * Constructor takes two criteria
        * `meetCriteria` should output whether the input item satisfies the criteria combination or not

**Composite pattern**. Work as a container of a collection of objects

**Decorator**. Have a child class working as an expansion of the base class, i.e. to add additional minor features to the base class

**Facade pattern**. Hide the complexities of the system, and provide an interface to the client, using which the client can access the system

**Flyweight pattern**. Act as a set of objects, i.e. no duplicate objects
* *Idea*. When user query for some object in the set, the factory will check if the object exists

    $\to$ If not, it creates the object then returns, otherwise, it returns the existing object

**Proxy pattern**. Provide a substitute or placeholder for another object

$\to$ A proxy controls access to the original object, allowing user to perform something before or after the request gets through to the original object

<div style="text-align:center">
    <img src="/media/73bA2fb.png">
    <figcaption>Illustration of proxy pattern</figcaption>
</div>

## Behavioral patterns

## J2EE patterns

# Appendix
## Discussion
**Basic difference between the factory and abstract factory design patterns**. Link [here](https://stackoverflow.com/questions/1001767/what-is-the-basic-difference-between-the-factory-and-abstract-factory-design-pat/35714637#35714637)
* *Factory*. Create objects without exposing the instantiation logic to the client
* *Factory method*. Define an interface for creating an object, but let the subclasses decide which class to instantiate
* *Abstract factory*. Provide an interface for creating families of related of dependent objects, without specifying their concrete classes

**Builder pattern and factory-related patterns**. https://gpcoder.com/4434-huong-dan-java-design-pattern-builder/

**Facade, proxy, adapter, and decorator patterns**.
* *Adapter*. Adapt a given class / object to a new interface
* *Facade*. A simple gateway to complicated set of functionality
* *Proxy*. Provide the same interface as the proxied-for class and typically does some housekeeping stuff on its own
* *Decorator*. Add more gunpowder to the objec