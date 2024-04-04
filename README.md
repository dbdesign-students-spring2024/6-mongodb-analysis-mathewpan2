# AirBnB MongoDB Analysis

[data](https://data.insideairbnb.com/belgium/vlg/antwerp/2023-12-27/data/listings.csv.gz)

This is data containing airbnb listings for the past 12 months since 12/27/23 within Antwerp, Belgium. This data comes from the site, [Inside Airbnb](https://insideairbnb.com/)

The file was originally in csv 



The data has no problems, but its very verbose and has many un-needed fields. So I got rid of any field that wasn't related to the assignment, to make the data easier to use.  

```python
keep = ["host_id", "host_is_superhost", "name", "price", "neighbourhood", "host_name", "beds", "neighbourhood_group_cleansed", "review_scores_rating"]
col_to_delete = []
for row in reader:
            if first_row:
                for index, category in enumerate(row):
                    if category not in keep:
                        col_to_delete.append(index)
                first_row = False
            row = [row[i] for i in range(len(row)) if i not in col_to_delete]
            writer.writerow(row)
```
In this code segement, I scan through the rows and add every column index I don't want into an array, and then when I write to a new csv file, I make sure to not add the indexes of the columns I don't want. This allows me to clean up the data and only be left with fields that are needed for this assignment.


| name                                                          | host_id | host_name          | host_is_superhost | neighbourhood                     | neighbourhood_group_cleansed | beds | price   | review_scores_rating |
|---------------------------------------------------------------|---------|--------------------|-------------------|----------------------------------|------------------------------|------|---------|----------------------|
| Boutique hotel in Antwerp · ★5.0 · 1 bedroom · 1 bed · 1 private bath | 234077  | Karin              | t                 |                                  |                              | 1    | $188.00 | 5.0                  |
| Rental unit in Antwerpen · ★4.79 · 1 bedroom · 2 beds · 1 bath | 1263933 | Kristien           | t                 | Antwerpen, Vlaams Gewest, Belgium |                              | 2    | $167.00 | 4.79                 |
| Rental unit in Antwerp · ★4.81 · 2 bedrooms · 2 beds · 1 bath | 1754396 | Marleen            | t                 | Antwerp, Flemish Region, Belgium |                              | 2    | $66.00  | 4.81                 |
| Rental unit in Antwerp · ★4.87 · 1 bedroom · 1 bed · 1.5 baths | 1835458 | Roos               | f                 |                                  |                              | 1    | $75.00  | 4.87                 |
| Rental unit in Antwerp · ★4.63 · 1 bedroom · 1 bed · 1.5 shared baths | 1820186 | Godelieve          | t                 | Antwerp, Flemish Region, Belgium |                              | 1    | $45.00  | 4.63                 |
| Rental unit in Antwerp · 1 bedroom · 2 beds · 1 bath          | 2562294 | Ahome              | f                 | Antwerp, Flemish Region, Belgium |                              | 2    | $282.00 |                      |
| Loft in Antwerp · ★4.81 · 1 bedroom · 1 bed · 1 bath          | 2987880 | Cédric             | t                 | Antwerp, Flanders, Belgium       |                              | 1    | $89.00  | 4.81                 |
| Rental unit in Antwerp · ★4.55 · 2 bedrooms · 3 beds · 1 bath | 462975  | Els                | t                 | Antwerp, Flemish Region, Belgium |                              | 3    | $156.00 | 4.55                 |
| Home in Antwerp · ★4.67 · 1 bedroom · 1 bed · 1 bath         | 3493319 | Glenn              | f                 |                                  |                              | 1    | $85.00  | 4.67                 |
| Loft in Antwerp · ★4.43 · 1 bedroom · 1 bath                 | 4050173 | Daisy              | f                 |                                  |                              |      | $146.00 | 4.43                 |
| Rental unit in Antwerp · ★4.67 · 1 bedroom · 1 bed · 1 bath  | 1735092 | Marc & Elizabeth   | f                 | Antwerp, Flemish Region, Belgium |                              | 1    | $99.00  | 4.67                 |
| Loft in Antwerp · ★4.83 · 1 bedroom · 2 beds · 1 bath        | 3424990 | Tim                | f                 | Antwerp, Flemish Region, Belgium |                              | 2    | $91.00  | 4.83                 |
| Rental unit in Antwerp · ★4.65 · 2 bedrooms · 3 beds · 1.5 baths | 4277604 | Sarah              | t                 | Antwerp, Flemish Region, Belgium |                              | 3    | $259.00 | 4.65                 |
| Boutique hotel in Antwerp · ★5.0 · 1 bedroom · 1 bed · 1 private bath | 234077  | Karin              | t                 | Antwerp, Flemish Region, Belgium |                              | 1    | $180.00 | 5.0                  |
| Rental unit in Antwerp · ★5.0 · 1 bedroom · 1 bed · 1.5 baths | 234077  | Karin              | t                 | Antwerp, Flemish Region, Belgium |                              | 1    | $214.00 | 5.0                  |
| Rental unit in Antwerp · ★4.82 · 1 bedroom · 1 bed · 1.5 baths | 4715596 | Caroline & Klaas   | t                 |                                  |                              | 1    | $85.00  | 4.82                 |
| Rental unit in Antwerp · ★4.60 · 3 bedrooms · 5 beds · 1 bath | 5446991 | Magali             | f                 |                                  |                              | 5    | $77.00  | 4.6                  |
| Rental unit in Antwerp · ★4.61 · 3 bedrooms · 5 beds · 1 bath | 5446991 | Magali             | f                 |                                  |                              | 5    | $77.00  | 4.61                 |
| Rental unit in Antwerp · ★4.52 · 1 bedroom · 2 beds · 1 bath  | 6068286 | Frédéric           | f                 |                                  |                              | 2    | $80.00  | 4.52                 |


1. 

```js
db.listings.find().limit(2)
```

This query displays the document containing the first 2 document found within the collection. No other function is done to the document, so it just displays the data of a listing in a json format.
```json
[
  {
    _id: ObjectId('660e7e234853e23b59bdcb8a'),
    name: 'Rental unit in Antwerpen · ★4.79 · 1 bedroom · 2 beds · 1 bath',
    host_id: 1263933,
    host_name: 'Kristien',
    host_is_superhost: 't',
    neighbourhood: 'Antwerpen, Vlaams Gewest, Belgium',
    neighbourhood_group_cleansed: '',
    beds: 2,
    price: '$167.00',
    review_scores_rating: 4.79
  },
  {
    _id: ObjectId('660e7e234853e23b59bdcb8b'),
    name: 'Rental unit in Antwerp · ★4.87 · 1 bedroom · 1 bed · 1.5 baths',
    host_id: 1835458,
    host_name: 'Roos',
    host_is_superhost: 'f',
    neighbourhood: '',
    neighbourhood_group_cleansed: '',
    beds: 1,
    price: '$75.00',
    review_scores_rating: 4.87
  }
]
```

2. 
```js
db.listings.find().limit(10).pretty()
```

This query lists the first 10 documents in can find in the collection, the pretty method is suppose to display the data in a more understandable format, but the results are same with or without it. 

```json
{
    _id: ObjectId('660e7e234853e23b59bdcb8a'),
    name: 'Rental unit in Antwerpen · ★4.79 · 1 bedroom · 2 beds · 1 bath',
    host_id: 1263933,
    host_name: 'Kristien',
    host_is_superhost: 't',
    neighbourhood: 'Antwerpen, Vlaams Gewest, Belgium',
    neighbourhood_group_cleansed: '',
    beds: 2,
    price: '$167.00',
    review_scores_rating: 4.79
  },
  {
    _id: ObjectId('660e7e234853e23b59bdcb8b'),
    name: 'Rental unit in Antwerp · ★4.87 · 1 bedroom · 1 bed · 1.5 baths',
    host_id: 1835458,
    host_name: 'Roos',
    host_is_superhost: 'f',
    neighbourhood: '',
    neighbourhood_group_cleansed: '',
    beds: 1,
    price: '$75.00',
    review_scores_rating: 4.87
  },
  {
    _id: ObjectId('660e7e234853e23b59bdcb8c'),
    name: 'Rental unit in Antwerp · ★4.63 · 1 bedroom · 1 bed · 1.5 shared baths',
    host_id: 1820186,
    host_name: 'Godelieve',
    host_is_superhost: 't',
    neighbourhood: 'Antwerp, Flemish Region, Belgium',
    neighbourhood_group_cleansed: '',
    beds: 1,
    price: '$45.00',
    review_scores_rating: 4.63
  },
```

3. 

```js
db.listings.find({
	"host_id": {
    "$in": [234077, 1754396]
  },
  "host_is_superhost": 't',
}, {
  "name": 1,
  "price": 1,
  "neighbourhood": 1,
  "host_name": 1,
  "host_is_superhost": 1,
  "_id": 0
})
```

This query searches for the listings from two hosts who are also super hosts, and displays certain amount of fields for each listing. This can help to give essential information about the listings under 2 hosts while hiding un-needed information.

```json
{
    name: 'Boutique hotel in Antwerp · ★5.0 · 1 bedroom · 1 bed · 1 private bath',
    host_name: 'Karin',
    host_is_superhost: 't',
    neighbourhood: 'Antwerp, Flemish Region, Belgium',
    price: '$180.00'
  },
  {
    name: 'Rental unit in Antwerp · ★4.81 · 2 bedrooms · 2 beds · 1 bath',
    host_name: 'Marleen',
    host_is_superhost: 't',
    neighbourhood: 'Antwerp, Flemish Region, Belgium',
    price: '$66.00'
  },
  {
    name: 'Rental unit in Antwerp · ★5.0 · 1 bedroom · 1 bed · 1.5 baths',
    host_name: 'Karin',
    host_is_superhost: 't',
    neighbourhood: 'Antwerp, Flemish Region, Belgium',
    price: '$214.00'
  },
```

4. 
```js
db.listings.distinct("host_name")
```

This query returns every listing with a unique hotname, essentially telling you how many people have made listings in the Antwerp region. This can help tell you how many unique people are actually making listings within a region, instead of just how many listings there are.

```json
'&Quot;La Casa Di Frà',
  'Abdulrahman',
  'AchA',
```

5. 
```js
db.listings.find({
  "beds": { "$gt": 2 },
   "neighbourhood": "Antwerpen, Vlaams Gewest, Belgium",
    "review_scores_rating": { "$ne": "", "$exists": true},
}, {
  "name": 1,
  "beds": 1,
  "review_scores_rating": 1,
  "price": 1,
  "_id": 0
}).sort({ "review_scores_rating": -1 })
```

This query finds all listings with more than 2 beds in a given neighborhood. This helps someone with a large party find an accomodating airbnb that's the right size for them. It's easier to see data like this compared to having look through each individual listing.




```json
{
    name: 'Townhouse in Antwerpen · ★5.0 · 3 bedrooms · 4 beds · 2 baths',
    beds: 4,
    price: '$200.00',
    review_scores_rating: 5
  },
  {
    name: 'Condo in Antwerpen · ★5.0 · 1 bedroom · 3 beds · 1.5 baths',
    beds: 3,
    price: '$150.00',
    review_scores_rating: 5
  },
  {
    name: 'Rental unit in Antwerpen · 2 bedrooms · 3 beds · 1 bath',
    beds: 3,
    price: '$75.00',
    review_scores_rating: 5
  },
```

6. 

```js
db.listings.aggregate([
  {
    $group: {
      _id: "$host_id",
      name: {$first: "$host_name"},
      total_listings: {$sum: 1}
    }
  }
])
```

This can help show you how many listings each host has. This can be useful when trying to gather how around how many airbnbs someone owns in the region that you're listing data is from. 

```json
{ _id: 94340401, name: 'Hendrik', total_listings: 2 },
  { _id: 55121527, name: 'Paul', total_listings: 1 },
  { _id: 164820738, name: 'Niksa', total_listings: 1 },
```


7. 

```js
db.listings.aggregate([
  {
    $match: {
      "review_scores_rating": { $ne: null }
    }
  },
  {
    $group: {
      _id: "$neighbourhood",
      avgRating: { $avg: "$review_scores_rating" }
    }
  },
  {
    $match: {
      avgRating: { $gte: 4 }
    }
  },
  {
    $sort: {
      avgRating: -1
    }
  }
])
```
This helps to tell you the highest rated region of airbnbs in your neighborhood. So you know which neighborhood has the best airbnbs, this would be very difficult to find out by just looking at the raw data.



```json
{ _id: 'Antwerp, Vlaanderen, Belgium', avgRating: 5 },
{ _id: 'Antwerpen, Flanders/Vlaanderen, Belgium', avgRating: 4.94 },
{ _id: 'Berchem, Antwerpen, Belgium', avgRating: 4.92 },
```