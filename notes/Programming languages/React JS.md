<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [React JS](#react-js)
  - [`<Route>` and `<Switch>` components](#route-and-switch-components)
<!-- /TOC -->

# React JS
## `<Route>` and `<Switch>` components
**`<Route>` component**. The most important component in React Router to understand and learn to use well
* *Idea*. The most basic responsibility of `<Route>` is to render some UI when its path matches the current URL
    * *Explain*. When the <Route>'s path matches the current URL, it renders its children
* *Example*. Consider the following code

    ```js
    import React from "react";
    import ReactDOM from "react-dom";
    import { BrowserRouter as Router, Route } from "react-router-dom";

    ReactDOM.render(
        <Router>
            <div>
            <Route exact path="/">
                <Home />
            </Route>
            <Route path="/news">
                <NewsFeed />
            </Route>
            </div>
        </Router>,
        node
    );
    ```

    If the location of the app is / then the UI hierarchy will be something like

    ```js
    <div>
        <Home />
        <!-- react-empty: 2 -->
    </div>
    ```

* *Route change*. If the same component is used as the child of multiple `<Route>`s at the same point in the component tree
    
    $\to$ React will see this as the same component instance and the component’s state will be preserved between route changes
    * *Disable route change*. If this is not desired
        
        $\to$ A unique key prop added to each route component will cause React to recreate the component instance when the route changes

**`exact` parameter in `<Route>`**. `exact` comes into play when we have multiple paths with similar names
* *Example*. Consider the following code

    ```js
    <Switch>
        <Route path="/users" component={Users} />
        <Route path="/users/create" component={CreateUser} />
    </Switch>
    ```

    * *Problem*. React router does partial matching, so `/users` partially matches `/users/create`
        
        $\to$ The router would incorrectly return the `Users` route
    * *Consequences*.
        * When we go to `http://app.com/users` the router will go through all of our defined routes
        
            $\to$ The first match will be returned
            * *Consequence*. The router would find the Users route first and then return it
        * When we go to `http://app.com/users/create`, the router would go through all of our defined routes
            
            $\to$ The first match will be returned
* *`exact` parameter*. Disable the partial matching for a route
    
    $\to$ This makes sure that it only returns the route if the path is an exact match to the current url
* *Revised example code*.
    
    ```js
    <Switch>
        <Route exact path="/users" component={Users} />
        <Route path="/users/create" component={CreateUser} />
    </Switch>
    ```

**`<Switch>` component**. Render the first child `<Route>` or `<Redirect>` matching the location
* *Difference from a bunch of `<Route>`s*. 
    * `<Switch>` renders a route exclusively
    * Every <Route> that matches the location renders inclusively