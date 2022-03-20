<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Nodejs - `require`, `exports`, and `module.exports`](#nodejs---require-exports-and-moduleexports)
  - [Module](#module)
- [Appendix](#appendix)
  - [Discussions](#discussions)
<!-- /TOC -->

# Nodejs - `require`, `exports`, and `module.exports`
## Module
**Module**. A separate program file in Nodejs

$\to$ When creating a module, it can be classified as a grouping of all related functions into a file

**Most common module formats**. There are many module formats in JavaScript but there are two formats that used almost in all JS projects
* *CommonJS (CJS) format*. Used in Node.js and uses `require` and `module.exports` to define dependencies and modules

    $\to$The `npm` ecosystem is built upon this format.
* *ES Module (ESM) format*. As of ES6 (ES2015), JavaScript supports a native module format
    * *Native module format*. Use an `export` keyword to export a module's public API and an `import` keyword to import it

>**NOTE**. We will talk about CommonJS format

**Requiring a module**. Node.js comes with a set of built-in modules, which we can use in our code without installation
* *Module import*. Require the module using the `require` keyword, and assign the result to a variable
* *Example*. Consider using the file system module and its `readdir` method

    ```js
    const fs = require('fs');
    const folderPath = '/home/jim/Desktop/';
    fs.readdir(folderPath, (err, files) => {
        files.forEach(file => {
            console.log(file);
        });
    });
    ```

* *Module import order in CommonJS*. Modules are loaded synchronously and processed in the order they occur

**Creating and exporting a module**.
* *Module creation*.

    ```js
    // user.js
    const getName = () => {
        return 'Jim';
    };
    const getLocation = () => {
        return 'Munich';
    };
    const dateOfBirth = '12.01.1982';
    exports.getName = getName;
    exports.getLocation = getLocation;
    exports.dob = dateOfBirth;
    ```

* *Module require*.

    ```js
    // index.js
    const user = require('./user');
    console.log(`${user.getName()} lives in ${user.getLocation()} and was born on ${user.dob}.`);
    ```

* *Module require with destructing assignment*.

    ```js
    const { getName, dob } = require('./user');
    console.log(`${getName()} was born on ${dob}.`);
    ```

**Export a default value**. When we have a module that exports just one thing

$\to$ It is more common to use `module.exports`

>**NOTE**. For sure we can use just `exports`

* *Example*.

    ```js
    // user.js
    class User {
        constructor(name, age, email) {
            this.name = name;
            this.age = age;
            this.email = email;
        }
        getUserStats() {
            return `
            Name: ${this.name}
            Age: ${this.age}
            Email: ${this.email}
            `;
        }
    }
    module.exports = User;
    ```

    ```js
    // index.js
    const User = require('./user');
    const jim = new User('Jim', 37, 'jim@example.com');
    console.log(jim.getUserStats());
    ```

# Appendix
## Discussions
**Difference between `module.exports` and `exports`**.
* *`module.exports`*. `module` is a contextual reference to the file we executed, e.g.

    ```js
    Module {
        id: '.',
        exports: {},
        parent: null,
        filename: '/Users/yaapa/projects/hacksparrow.com/run.js',
        loaded: false,
        children: [],
        paths: [
            '/Users/yaapa/projects/hacksparrow.com/node_modules',
            '/Users/yaapa/projects/node_modules',
            '/Users/yaapa/node_modules',
            '/Users/node_modules',
            '/node_modules' 
        ] 
    }
    ```

    $\to$ `exports`, which is an empty object by default, defines the importable objects of our module

* *`exports`*. `exports` is a reference to `module.exports`
    * *Example*. 

        ```js
        // index.js
        exports.firstName = "Ibrahim";
        exports.lastName = "AlRayyan";
        ```

        will results in

        ```js
        Module {
            id: '.',
            exports: { firstName: 'Ibrahim', lastName: 'AlRayyan' },
            ...
        ```

**`require` and module cache**. When the `require()` function is called to the same module in multiple files

$\to$ The module has to be loaded once only
* *Explain*. Next time a `require()` function is called on the same module then pulls from the cache
* *Needs for synchronous import*. `require()` loads modules synchronously
    * *Explain*. Otherwise we could not access the objects in the correct order
        
        $\to$ Synchronous behavior is required while requiring modules from one file to another