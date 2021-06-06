---
title: ReactJS tutorial
tags: Programming languages
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [ReactJS tutorial](#reactjs-tutorial)
  * [Introduction](#introduction)
  * [Overview](#overview)
    * [Passing data through props](#passing-data-through-props)
    * [Making an interactive component](#making-an-interactive-component)
    * [Changing data in React](#changing-data-in-react)
    * [Function components](#function-components)
    * [Key in react](#key-in-react)
* [Appendix](#appendix)
  * [References](#references)
  * [React terminologies](#react-terminologies)
  * [Tricks and advice](#tricks-and-advice)
  * [React libraries](#react-libraries)
<!-- /TOC -->

# ReactJS tutorial
## Introduction
**Quick compile React code**. [CodePen.io](https://codepen.io/gaearon/pen/oWWQNa?editors=0010)

**React**. A declarative, efficient, and flexible JS library for building UIs
* *Idea*. Complex UIs are composed of components
* *Example code*.

```javascript=
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class ShoppingList extends React.Component {
  render() {
    return (
      <div className="shopping-list">
        <h1>Shopping List for {this.props.name}</h1>
        <ul>
          <li>Instagram</li>
          <li>WhatsApp</li>
          <li>Oculus</li>
        </ul>
      </div>
    );
  }
}
```

**React component class**. Also called React component type
* *Inputs*. Paremeters, called `props`
* *Outputs*. A hierarchy of views to display via the `render()` method
    * *`render()` method*. Return a React element, i.e. a lightweight description of what to render

        $\to$ React takes this element and display the result

## Overview
### Passing data through props
```javascript=
class Board extends React.Component {
    renderSquare(i) {
        return <Square value={i} />
    }
}

class Square extends React.Component {
    render() {
        return (
            <button className="square">
                {this.props.value}
            </button>
        );
    }
}
```

### Making an interactive component
**Naive code**.

```javascript=
class Square extends React.Component {
    render() {
        return (
            <button className="square" onClick={function() { alert ("click"); }}>
                {this.props.value}
            </button>
        );
    }
}
```

**Good practice**. To save typing and avoid confusing behavior of `this`, we will use the arrow function syntax, i.e.

```javascript=
class Square extends React.Component {
    render() {
        return (
            <button className="square" onClick={() => alert("click")}>
                {this.props.value}
            </button>
        );
    }
}
```

**Element state**. We can save the state of an element to `state` property

>**NOTE**. `this.state` should be considered as private to a React component that it's defined in

* *Example*.

    ```javascript=
    class Square extends React.Component {
        constructor(props){
            super(props);
            this.state = {
                value: null,
            };
        }

        render() {
            return (
                <button
                    className="square"
                    onClick={() => this.setState({value: "X"})}
                >
                    {this.props.value}
                </button>
            );
        }
    }
    ```

>**NOTE**. In JS classes, we need to always call `super` when defining the constructor of a subclass

>**NOTE**. All React component classes having a `constructor` should start with a `super(props)` call

>**NOTE**. When we call `setState` in a component, React automatically updates the child components inside of it too
>
### Changing data in React
**Approaches**.
* *First apporach*. Directly change the data's values
    * *Example code*.

    ```js=
    var player = {score: 1, name: "Jeff"};
    player.score = 2;
    ```

* *Second apporach*. Replace the data with a new copy which has the desired changes
    * *Example code*.

    ```js
    var player = {score: 1, name: "Jeff"};
    var newPlayer = Object.assign({}, player, {score: 2});
    ```

    * *Advantages*.
        * Make complex features much easier to implement
            * *Explain*. Avoiding direct data mutation lets us keep previous versions of the game's history intact, and reuse them later
        * Detecting changes in mutable objects is difficult since they are modified directly
        * Determining when to re-render in React, thus we can build pure components in React
            * *Explain*. Immutable data can easily determine if changes have been made, which helps to determine when a component requires re-rendering

### Function components
**Function components**. a simpler way to write components, which only contain a `render` method and don't have their own state
* *Idea*. Instead of defining a class extending `React.Component`

    $\to$ We write a function taking `props` as input and returns what should be rendered
* *Example code*.
    * *Define a function `Square`*.

    ```js=
    function Square(props){
        return (
            <button className="square" onClick={props.onClick}>
                {props.value}
            </button>
        );
    }
    ```

    >**NOTE**. `this.props` is now `props` since this is not an object

    * *Use `Square` function in `Board`*:

    ```js=
    renderSquare(i) {
        return (
            <Square
                value={this.state.squares[i]}
                onClick={() => this.handleClick(i)}
            />
        );
    }
    ```

### Key in react
**Key**. Each child in an array or iterator should have a unique `key` prop

**Key and list**.
* *Example*. Consider `<li key={user.id}> {user.name}: {user.taskCount} tasks left</li>`
    * *When we render a list*. React stores some information about each rendered list item
    * *When we update a list*. React needs to determine what has changed, e.g. we could have added, removed, re-arranged, or updated the list’s items
* *Purpose of keys*.
    * We need to specify a key property for each list item to differentiate each list item from its siblings
    * When a list is re-rendered, React takes each list item’s key and searches the previous list’s items for a matching key
        * If the current list has a key that didn’t exist before, React creates a component
        * If the current list is missing a key that existed in the previous list, React destroys the previous component
        * If two keys match, the corresponding component is moved
    * Keys tell React about the identity of each component which allows React to maintain state between re-renders. If a component’s key changes, the component will be destroyed and re-created with a new state
* *Example*. Use keys `alexa`, `ben`, `claudia`, etc.

    >**NOTE**. If we are display data from a database, database IDs could be used as keys

**Key in React**. `key` is a special and reserved property in React (along with `ref`, a more advanced feature)
* When an element is created, React extracts the `key` property and stores the key directly on the returned element
* Even though `key` may look like it belongs in `props`, `key` cannot be referenced using `this.props.key`. React automatically uses `key` to decide which components to update

>**NOTE**. A component cannot inquire about its key

>**NOTE**. It’s strongly recommended that you assign proper keys whenever you build dynamic lists
>* *Explain*. If you don’t have an appropriate key, you may want to consider restructuring your data so that you do

**Array index as key**. If no key is specified, React will present a warning and use the array index as a key by default
* *Drawback*. Using the array index as a key is problematic when trying to re-order a list’s items or inserting/removing list items

>**NOTE**. Explicitly passing `key={i}` silences the warning but has the same problems as array indices and is not recommended in most cases

>**NOTE**. Keys do not need to be globally unique; they only need to be unique between components and their siblings

# Appendix
## References
* JS:
    * https://developer.mozilla.org/en-US/docs/Web/JavaScript
    * https://javascript.info/
* React GUI:
    * https://material-ui.com/?fbclid=IwAR3CQmqOdFVlf6McdozElyophEyMnNWBe0R6DkPuoAXNwU64fMdnbLUtcsQ
    * https://ant.design/docs/react/introduce?fbclid=IwAR34a1R4dB_lWHsw_R2mfj_ggEbG5WCJbp4ub6kpGYNTHfgLfYQj76akstc

## React terminologies
* Controlled components: components which do not maintain state, they receive values and inform the controller component when they are clicked (or something similar)
* Long Ke's advice: swe thì quan trọng nhất là biết flexbox, grid, mấy tag margin, padding... để xếp layout các component thôi

## Tricks and advice
* Tools to quickly write web front-end: https://codepen.io/
* To collect data from multiple children, or to have two child components communicate with each other, you need to declare the shared state in their parent component instead
    * Explain: The parent component can pass the state back down to the children by using props

    $\hspace{1.0cm} \rightarrow$ This keeps the child components in sync with each other and with the parent component
* Unlike the array `push()` method you might be more familiar with, the `concat()` method doesn’t mutate the original array, so we prefer it
* IN JS, we can use `map()` method of arrays to map data to other data
    * Example code 1:

    ```js
    const numbers = [1, 2, 3];
    const doubled = numbers.map(x => x * 2); // [2, 4, 6]
    ```

    * Example code 2:

    ```js
    const numbers = [1, 2, 3];
    const doubled = numbers.map(x => {
        const factor = 2;
        return x * factor;
    }); // [2, 4, 6]
    ```

## React libraries
* React Fragment to return multiple elements in `render()`
* React Route DOM for routing between pages
* React Helmet to manage `<head>
