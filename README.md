## Nobitex python api

###installation
```
pip install NobitexAPI
```

### working with package

```
from NobitexAPI import Nobitex
nt = Nobitex('your nobitex email' , 'your nobitex password')
```

####calling object functions
```
print(nt.global_market_stats())
```

for more info please check [nobitex docs](https://apidocs.nobitex.ir/#82d68ae596)