# CDC Source Normallization Guidelines

When following our guide on creating new CDC Source modules and our data models, you might come across situations where your specific mapping case is inique and hasn't been addressed in any other modules. While NTerminal is a very flexible system that will accept any data you throw at it, it is important to adhere to a few simple rules to make it easier to discover and use the data produced by your module.

## Symbol

Unless you are working with natural language data, your fileds will most likely be associated with specific coins/crypto projects. Clearly identifying that project and assigning a proper value to the field `symbol` is therefore extremely important. For example, when working with data from [ZCash stats from bitinfocharts](https://bitinfocharts.com/zcash/), you would assign `ZEC` as the value to your `symbol` field.

## Value format

As different sources display the same information in different formats, it's important to specify the format in the name of the field. For example, when working with data from [ZCash stats from bitinfocharts](https://bitinfocharts.com/zcash/), you would create `market_capitalisation_USD` field and assign `707906541` value to it instead of `market_capitalisation = $707,906,541 USD`.