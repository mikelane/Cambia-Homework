# Cambia Takehome Interview: Writeup

#### Michael Lane

## Gherkin

> Explain in detail why Gherkin tests might be helpful in the future

Automated BDD testing with Gherkin is useful because it provides a way to automate acceptance testing. Moreover, tests defined with Gherkin give non-technical stakeholders a way to define a full accounting of the set of features of the system. Automated testing of all of the features in a given system gives confidence that the application does exactly what it is supposed to do.

Gherkin tests can serve the broader purpose of focusing the development of the software and preventing scope creep. When software development is guided by Gherkin tests, the feature requirements are explicit, well defined, and clear to technical and non-technical stakeholders alike. Additionally, Gherkin tests help define integration tests around specific features.

## Tools
1. Version control systems are, obviously, helpful at keeping track of changes in a given system. New changes that cause problems can be identified and corrected quickly and easily. Good version control systems like Git also make the process of working with other engineers on the same product much more convenient and less prone to errors. 

    There is a bit of a learning curve when it comes to using a VCS. Someone who is new to VCS could cause big problems if care is not taken to protect access to the main branch. Also, wading through a sea of micro-commits can be tedious, so a good merge strategy is important. When there are lots of big changes in a given branch, dealing with conflicts can be a nightmare.

2. Docker is excellent at allowing the developer to create pristine, isolated, and repeatable environments. Setting up a python environment, for example, can be a lot more troublesome than one expects. However, using docker, one can simply create a container that is based on an official Python container with the OS and python version the developer desires. It follows taht Docker is also an excellent way to ensure that the code that works in development will also work in production. 

    Docker is not without quirks. It can take a bit of time to rebuild the container when changes are made. Also, some extra tooling, *e.g.* entrypoint scripts, are often required to help accomplish certain tasks that would be simple in code run outside of a container. Also, there is a steep learning curve (and not-so-great documentation) when it comes to learning how to use Docker.

3. When choosing a language for a given task, the biggest factor is to choose a language that can accomplish the task. Some tasks are not well suited to certain languages. Someone writing firmare code probably would not be very successful using a high-level scripting language, for example. On the other hand, even though C is a good choice for embedded software engineering, it is a particularly poor choice for writing the back end of a web server. 

    Often times, there is not a clear choice. There are many web back ends written in Java, Ruby, Node.js, Python, etc., and any one of them could be re-written from the ground up in a different language. And that brings up the next consideration: what is primarily being used for a given project. If an entire web application is written in Java, then it makes no sense to start a new part of that application in Python. Even if there are certain advantages of one language over another, when an organization has focused on a given language, there is a lot of organizational knowledge about that language. That fact alone is good reason to choose the language of choice for a given organization.
    
    That said, when writing new code for a project that has a strict time limit, like this homework does, it's probably best to choose the language you're most familiar with (assuming that language can get the job done, of course). Since I'm most comfortable in Python and since Python can most certainly get the job done with this homework, the choice to use Python was not so difficult for me.
    
## Testing Methodology

1. The software development cycle can be broken into a few broad steps:
    1. **Inception:** The software is requested and the stakeholders plan the basic architecture.
        - QA helps devise the initial basic set of requirements
        - QA sets up the system test environment based on those requirements
    2. **Construction:** The requirements are solidified and engineering work begins.
        - QA engineers validate that the developed components meet the rquirements
    3. **Transition:** Software development and testing is complete and the system goes live. 
        - QA engineers test that the system functions properly before it goes live

2. In the 2 weeks before the team starts writing software, QA must help solidify the requirements. Also the QA engineer should set up the testing frameworks, *e.g.* Gherkin tests, and perhaps ensure the testing portions of the CI/CD pipelines are established.

3. Running tests manually is okay when the number of tests is small and the complexity of the tests is low. When there are a lot of tests or when the tests are complicated, when there is a specific ordering required, when there are high-priority tests that cannot be forgotten, when multiple tests need to be run at once, or when the size of the data being tested is large, automated testing can help ensure the testing is effective.

4. Integration tests should be focused on testing the overall system environment. If the unit tests really are good, then they will be validating the correctness of individual methods and objects. Integration tests, unlike unit tests, should test external resources like networks, databases, and filesystems. Integration tests should be more complex and may require additional tooling or infrastructure. 

    That is to say that integration tests should not be testing at the level of the individual units. With integration testing, QA should have a broader focus. With a unit test of a database insert, for example, verifying that an insert happens on an in-memory database is sufficient. However, an integration test would want to spin up an instance of the database that will be used in production and validate several systems, *e.g.* the database connection module, the search module, etc., all in the same test.