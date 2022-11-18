# Weather Pipeline

## To Run

create a .env file and put accuweather api key at root level, using key

```
accuweather-api-key
````

then run

``` 
source ./setup.sh
```

````
make run location=stockholm
`````

the current weather record will be saved as avro in /records folder.


