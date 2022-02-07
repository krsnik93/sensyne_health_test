## Backend Engineer - Tech Test

### Introduction

Your goal in this task is to implement a simple back-end service for an online marketplace.  Here is a sample of some of the products available on the site.


| Product code  | Name  |  Price |
|---|---|---|
|  001 |  Lavender heart | £9.25  |
|  002 |  Personalised cufflinks | £45.00  |
|  003 |  Kids T-shirt | £19.95 |

Your task is to create a RESTful API to implement CRUD operations on this data.  You should provide five endpoints: 

* GET /products - A list of products, names, and prices in JSON.
* POST /product - Create a new product from a JSON body.
* GET /product/{product_id} - Return a single product by id in JSON.
* PUT /product/{product_id} - Update a product's name or price by id.
* DELETE /product/{product_id} - Delete a product by id.

### Implementation

The service may be implemented in either Node.js or Python using whatever framework (e.g. Express or Flask) you prefer.  Use Swagger/OpenAPI to document how to interact with your API.  Make sure there are sensible status codes in the response for both successful and unsuccessful requests (e.g. the service should report a code such as 404 for an unknown product ID, and not simply error out).

Use a database for persistence, though the technology you use is your own choice; you may also use any publicly-available (installable through normal package managers or build systems) ORMs, etc.

Note: We estimate this task should take no more than 1-2 hours. If it is taking you significantly longer than this, tidy up what you have and then submit it. This is not supposed to be a task to test your endurance and your work and thoughts will provide a valuable discussion point in any interview.

### Requirements

* Submit your completed solution either either as a git repository (using a public repo service such as Github or Bitbucket), or as a zip file (making sure you include the .git directory). Commit early and often rather than in a single large commit; trial and error is acceptable and even encouraged as it really helps us capture your thinking.

* Your solution should contain instructions sufficient to allow a technical user to install and run your app (ideally a README.md including, e.g. a lockfile or requirements.txt, or any build scripts).  

* A collection of Postman tests will be provided to you with this document, and will be run against your service to verify the results.  Be sure to seed your database with the sample data in the table above before running the tests.

* A successful submission will pass all of the functional Postman tests.  You will be evaluated on providing a working API as well as basic code style, simplicity, and correctness.  You will not be evaluated on the API’s robustness or performance, and you do not need to worry about production server setup (i.e. a framework’s default server in debug mode is fine). 

### Notes and suggestions

Bonus points / extensions (not required for a passing solution):
* Containerise the solution using Docker
* Demonstrate a couple of good unit tests, using mocking where appropriate
* Provide a Makefile, e.g. to run the tests
