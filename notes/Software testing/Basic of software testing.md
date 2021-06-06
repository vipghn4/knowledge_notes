---
title: Basic of software testing
tags: Software testing
---

# Table of Contents
[toc]

# Software testing life cycle
## Phases and activities
**Requirements analysis**. Review the business and software requirements and identify any defects in the specifications
* *Work product*. Review defect reports

**Test planning**. Once we have a general idea of what needs to be tested, we plan for the tests
* *Work product*. Test plan, test estimation, and test schedule

**Test designing**. Design tests on the basis of detailed requirements / design of the software
* *Work product*. Test cases, test scripts, test data, and requirements traceability matrix

**Test environment setup**. Setup the test environment, e.g. server, client, network, etc., with the goal of replicating the end-users' environment
* *Work product*. Test environment

**Test execution**. Execute the test cases and scripts in the test environment to see whether they pass
* *Work product*. Test results, and defect reports

**Test reporting and closure**. Prepare various reports for various stakeholders
* *Work product*. Test results, test metrics, and test closure report

## Testing principles
* Testing shows the presence of defects, not their absense
* Exhaustive testing is impossible
    * *Explain*. There is an infinite number of scenarios, environments, and paths to
        
        $\to$ It is technically impossible to test all of them
* Early testing saves time and money
* Defects cluster together
    * *Explain*. 80% of outcomes result from 20% of all causes for any given event holds true in software development
* Be aware of the pesticide paradox
* Testing is context dependent
* Absense of errors is fallacy

# Software testing methods
**Testing methods**.
* *Static testing*. Work products are reviewed without executing them
* *Dynamic testing*. The behavior of work products is evaluated  by executing them
* *Black box testing*. Internal structure / design / implementation of the item being tested is not known to the tester
* *White box testing*. Internal structure / design / implementation of the item being tested is known to the tester
* *Gray box testing*. Internal structure / design / implementation of the item being tested is partially known to the tester
* *Agile testing*. Software testing method which follows the principles of agile osftware development
* *Ad hoc testing*. Testing without any planning and documentation
* *Manual testing*. Software is tested manually by human
* *Automated testing*. Software is tested with the help of scripts and tools

## Static testing
**Static testing**. Enable early detection of defects before dynamic testing is performed

>**NOTE**. Developers should prioritize static testing as much as they dynamic testing they desire an all-round assurance of quality

**Objectives**.
* Identify and correct defects in requirements to prevent defects in design or code
* Identify and correct defects in test cases, test scripts, test data, and prevent false positives / false negatives
* Identify defects which are not easily found by dynamic testing
* Reduce cost of quality over software's lifetime
* Improve team communication and collaboration

**Work products**. Static testing can be applied to any work product. The following are major ones
* Requirements (business and software)
* Architecture and design
* Mockups
* Code
* Test artifacts, e.g. test plan, test acse, test script, and test data
* User guides

**Types**.
* *Review*. Find defects, and generate new ideas or solutions
* *Walkthrough*. A tour or demonstration of a work product

    $\to$ This can find defects, generate new ideas or solutions, gather improvements suggestions or provide training
* *Inspection*. A careful examination or scrunity of a work product
    * *Purpose*. Find defects, evaluate quality standards, assess individual performance, or identify process improvement areas
    * *Conduction*. Formally with a defined process and documentation, by seniors or experts and more rigorous than reviews

**Guidelines**. 
1. Make sure the objectives of each static testing are clear
2. Clarify the roles and responsibilities of each person involved
3. Select the specific static testing type, i.e. review, walkthrough, or inspection, appropriate to the type and level of work products and participants

**Tricks**.
* Start static testing early   
* If the work product is large, divide them into chunks and begin from the first chunk itself
* Create and use checklists as much as possible
* Conduct static testing as formally as possible, with defined process and documentation
* Give enough time to participants for preparation and schedule sessions with adequate notice
* Integrate static testing in the company's policies / procedure so that there is organizational buy-in

## Dynamic testing
**Dynamic testing**. Enable the examination of perceivable responses from the software to inconstant variables that can change with time
* *Idea*. Provide inputs to the software under test and check if the output is as expected

    >**NOTE**. The execution can be either manual or automated

* *Level*. Unit testing, integration testing, system tesing, and acceptance testing

### Types
**Functional testing (feature testing)**. Feed the functions input and examine the output
* *Purpose*. Ensure that the requirements are properly satisfied by the application

>**NOTE**. Functional testing is more effective when the test conditions are created directly from user / business requirements
>* *Explain*. When test conditions are created from the system documentation
>$\to$ The defects in that documentation will not be detected through testing

**Smoke testing (build verification testing)**. Comprise of a non-exhaustive set of tests aiming at ensuring that the most important functions work
* *Purpose*. 
    * Decide if a build is stable enough to proceed with further testing
    * Decide whether to announce a production release or to revert
    * EXpose integration and major problems early in the cycle
* *Smoke test*. A test suite that covers the main functionality of a component or system to determine whether it works properly before planned testing begins
* *Elaboration*. Cover most of the major functions of the software but none of them in depth
* *Conduction*. On both newly created software and enhanced software, performed manually or with the help of automation tools or scripts

    >**NOTE**. If builds are prepared frequently and
    >$\to$ It is best to automate smoke testing

>**NOTE**. Do not consider smoke testing to be a substitute for functional testing or regression testing

**Confirmation testing (re-testing)**. Conducted to confirm that a defect has been fixed

$\to$ Confirmation testing is performed after fixing a defect to confirm that a failure caused by that defect does not reoccur
* *Elaboration*. If a defect is identified and fixed, a new version of software is provided

    $\to$ The test case that failed is executed again to confirm if the defect is actually resolved and if the test case now passed

**Regression testing**. Intend to ensure that changes (enhancements or defect fixes) to the software have not adversely affected it
* *Purpose*. Detect whether defects have been introduced or uncovered in unchanged areas of software
* *Elaboration*. During regression testing, new test cases are not created but previously created test cases are re-executed

    >**NOTE**. "regression" literally means the act of going back to a previous place or state

* *Methods*. Black box or white box testing, manually or automated (highly recommended)
* *Types*.
    * *Full regression test*. The entire regression test suite is run to ensure that the change has not affected any part of the software

        $\to$ This is costly in terms of time and effort and may not always be feasible
    * *Partial regression test*. Certain test cases are selected and run while others are left out
        * *General prioritization*. Prioritize test cases based on 
            * Business impact 
            * Critical features
            * Frequently used functionalities
            * Complex implementation and buggy areas of the software
        * *Version-specific prioritization*. Prioritize test cases based on 
            * What changes have been made in the version of software
            * The likely areas in the software that might have been impacted due to those changes

**Non-functional testing**. The system is tested against the non-functional requirements, e.g. usability, performance, security, and compliance
* *Methods*. White box testing (normally) and automated (except for usability testing)

**Performance testing**. Determine how a system performs in terms of responsiveness and stability under a certain load
* *Focus attributes*. Performance testing mainly focuses on the following software quality attributes
    * *Responsiveness*. The ability of software to respond quickly or complete assigned tasks within a reasonable time
    * *Concurrency*. The ability to service multiple requests to the same resources at the same time
    * *Reliability*. The ability of software to perform a required function under stated conditions for the stated priod of time without any errors
    * *Stability*. The ability of software to remain stable under varying loads or over time
    * *Scalability*. The measure of software's ability to increase or decrease in performance in response to changes in software's processing demands
* *Types*.
    * *Load testing*. Evaluate the behavior of a system at increasing workload
    * *Stress testing*. Evaluate the behavior of a system at or beyond the limits of its anticipated workload
    * *Endurance testing*. Evaluate the behavior of a system when a significant workload is given continuously
    * *Spike testing*. Evaluate the behavior of a system when the load is suddenly and substantially increased
* *Tips*.
    * Establish a test environment as close to the production environment as possible
    * Isolate the test environment even from the QA or UAT environment
    * Though there is no perfect tool for performance testing, research and decide on the tool that best fits your purpose
    * Do not rely on the results of one test

        $\to$ Conduct multiple tests to arrive at an average number

**Security testing**. Test the security of the system

**Compliance testing**. Determine the compliance of the component or system with internal or external standards

## Black box testing
**Purposes**. Find errors in the following categories
* Incorrect or missing functions
* Interface errors
* Errors in data structures or external database access
* Behavior or performance errors
* Initialization and termination errors

**Levels**. Integration testing, system testing, and acceptance testing

**Techniques**.
* *Equivalance partitioning*. 
    1. Divide input values into valid and invalid partitions
    2. Select representative values from each partition as test data
* *Boundary value analysis*.
    1. Determine boundaries for input values
    2. Select values which are at the boundaries and just inside / outside of the boundaries as test data
* *Cause-effect graphing*. 
    1. Identify the cases (input conditions) and effects (output conditions)
    2. Produce a cause-effect graph
    3. Generate test cases accordingly to the graph

**Pros and cons**.
* *Pros*.
    * Tests are done from a user's point of view, and will help in exposing discrepancies in the specifications
    * Tester need not know programming languages or how the software has been implemented
    * Tests can be conducted by a body independent from the developers

        $\to$ This allows for an objective perspective and the avoidance of developer-bias
    * Test cases can be designed as soon as the specification are complete
* *Cons*.
    * Only a small number of possible inputs can be tested and many program paths will be left untested
    * Without clear specifications, which is situation in many projects, test cases will be difficult to design
    * Tests can be redundant if the software designer / developer has already run a test case

## White box testing
**White box testing**. Exercise paths through the code and determine the appropriate outputs

**Levels**. Unit testing, integration testing, and system testing

**Pros and cons**.
* *Pros*.
    * Testing can be commenced at an earlier stage, without GUI available
    * Testing is more thorough, with the possibility of covering most paths
* *Cons*.
    * Tests can be very complex, highly skilled resources are required, with thorough knowledge of programming and implementation
    * Test script maintenance can be a burden if the implementation changes too frequently
    * Tools to cater to every kind of implementation / platform may not be readily available

## Agile testing
**Agile testing**. Testing must be conducted at the initial stages of (almost parallel to) development

>**NOTE**. Agile testing is not sequential but is a continuous process

# References
* [Software testing fundamentals](https://softwaretestingfundamentals.com/software-testing-life-cycle/