# AFEX Backend Dev Test

### Your Task

1. Get this app to work
2. Change the database config to use PostgreSQL
3. Config settings for dev, staging and production servers
4. Add Two(2) security updates to the settings file

A Django app has been created under `/apps/` called `crm`

1. Configure this app to work with the main project
2. Two models has been created for you: "Client" and "ClientWallet":
   a. Write a CRUD option with the Client Model
   b. Write a PUT/POST option for the Client Wallet model (i.e ability to fund a particular client's wallet)
   c. Write/Configure API endpoints to fetch client (including their wallet balance)
   N:B You are to design an appropriate frontend for task in a & b above
3. Set-up a web socket for the client wallet model
4. Write a background task that populates the Client model with users from this [endpoint](https://62c2c06cff594c656764970a.mockapi.io/users). This task should run every hour.

\*\*\* Optional

1. Configure Docker for this project
