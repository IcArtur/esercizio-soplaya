### Notes about the exercise:
1) I would ask many details to a client that gives me this CSV, I'm making up all the information that are missing.
2) The difference of hours and money can be both DB field or properties, not knowing the usage rate of those
information I'm going to pick one of those two.
3) I am assuming that the dataset.csv file is in the root of the project.
4) It is not specified how to filter for date ranges. I used two query params: start_date and end_date. To filter we can
 use both of them, only one or none.
5) There are no docstring in this project: this is a simple project, I have not used them for shortage of time.

### How to run the project:

1. Run the `setup_project.sh` script in the root folder.

2. Execute the command `python manage.py import_dataset` to import the CSV file. If no positional parameters are specified, it will take the `dataset.csv` file that I have conveniently left in the repository. If you prefer to use a different file, you can use a positional parameter by specifying the absolute path of the CSV file. The second positional parameter is the batch size of rows to import.

3. At this point, the system is up and running with the data inside. Start the Django server with the command `python manage.py runserver 0.0.0.0:8000`.

4. The requested API is complete with all mandatory and optional requests. The endpoint is, assuming we're in local:
   `0.0.0.0:8000/v1/restaurants`
   
   and these are the available query parameters:
   - `start_date`: Filter from this date onwards (inclusive), format `YYYY-MM-DD`.
   - `end_date`: Filter up to this date (inclusive), format `YYYY-MM-DD`.
   - `order_by`: Sort the results based on a field. The fields available are those present in the CSV plus the two calculated fields `money_difference` and `hours_difference`.
   - `sort_order`: Choose ascending (`asc`) or descending (`desc`) order once a field is selected to sort the results. The default is `desc`.
```
