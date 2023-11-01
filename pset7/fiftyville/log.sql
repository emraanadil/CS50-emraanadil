-- Keep a log of any SQL queries you execute as you solve the mystery.

-- check the tables that are available
-- select description from crimetable
-- 28 July 2020 theft took place
-- theft time: 10:15am  at chamberlin street courthouse;
-- interview with 3 persons , keyword = courthouse;
-- 10 minutes after theft thief get into car in the courhouse parking and drive away
-- at morning thief withdrawing money from atm at fifer street
-- called someone call duration: less than a minute;
-- flight out of fiftyvalle earliest flight, on 29 July 2020, purchased the flight ticket.

   select name from people join bank_accounts on bank_accounts.person_id = people.id
   where bank_accounts.account_number in (select account_number from atm_transactions
   where year = 2020 and month = 7 and day = 28
   and atm_location = "Fifer Street" and transaction_type = "withdraw")
   intersect
   select name from people where license_plate in (select license_plate
   from courthouse_security_logs where month = 7 and  day = 28 and hour = 10
   and  minute >15 and minute < 25  AND activity = "exit")
   intersect
   select name from people
   where phone_number in (select caller from phone_calls
   where month = 7 and day = 28 and duration < 60)
   intersect
   select name from people join passengers on people.passport_number = passengers.passport_number
   where flight_id = (SELECT id from flights where day = 29 and month = 7 and year= 2020
   order by hour, minute limit 1);

   --Departure city
   select city from airports where id =
   (select destination_airport_id from flights where day = 29 and month= 7 and year = 2020
   order by hour,minute limit 1);

   --find partner;
   select name from people join phone_calls on phone_calls.receiver = people.phone_number
   where day = 28 and month = 7 and duration < 60
   and caller = (select phone_number from people where name = "Ernest");




-- Ernest
-- Madison
-- Russell