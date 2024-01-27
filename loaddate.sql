CREATE TABLE "User" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "email" VARCHAR,
  "password" VARCHAR,
  "is_staff" BIT
);
CREATE TABLE "Orders" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "datetime" DATE,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE "OrdererdDrinks" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "drink_id" INTEGER,
  "order_id" INTEGER,
  "preference_id" INTEGER,
  FOREIGN KEY(`drink_id`) REFERENCES `Drinks`(`id`),
  FOREIGN KEY(`order_id`) REFERENCES `Orders`(`id`),
  FOREIGN KEY(`preference_id`) REFERENCES `Preferences`(`id`)
);
CREATE TABLE "Drinks" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" VARCHAR
);
CREATE TABLE "Preference" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "temperature" VARCHAR
);