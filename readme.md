Assignment 1
   I have created a simple piple line which transfers the data from json to mongodb using script data insertion.

   Postgresql and mongodb both are docker based services.

   Once the data is inserted in mongodb, then batch wise it reads the mongodb data and stores it in postres sql db.

   Data batch processing is done by main script (main_batch_processing).


Assignment 2
   I have used existing ppostresql docker service to store consumer data.
   We have created new table for this.
   Basic configuration of kafka was required for publish/subscribe model.
   First run consumer.py file and then producer.py
   Once consumer consumes data from json via producer that data is stored is postgres tables. 


Bonus 

1. Input checks and validations can be done using if and if isinstance(var and tpe)
2. I have use primary key constraints so i have maintained data integrity.
3. In Json already nested fields exist but if more nested then we have to 
   go down step wise and fetch data from json document.
Design :
   Upload service :
      UPLOAD SERVICE ---> MONGODB  -----> Caching Data(Cache data once and process it n times.)
                             |
                             |
                             |
                             V
                          POSTRESQL
      We can apply sharding and partitioning and indexes for mongodb and postresql for storing data fast

   Pub/Sub Service:
         Producers ---topic---> consumers -----> Postrsql


I have coded with the best of my understanding and knowledge even more devlopments, debbuging and testing
Could have been possible if time and technology was not limited.
