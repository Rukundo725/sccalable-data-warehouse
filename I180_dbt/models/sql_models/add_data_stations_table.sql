
with source_stations_table as (
  SELECT ID, Name, Lanes, Length, State_PM, Abs_PM
  FROM {{ source('i80_davis', 'stations_table')}}
  LEFT OUTER JOIN {{ source('i80_davis', 'stations_table')}}
  ON {{ source('i80_davis', 'stations_table')}}.ID={{ source('i80_davis', 'stations_table')}}.source_id
)

SELECT * FROM stations_table