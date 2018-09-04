# Data Analysis

### Data file
all data file is shown with utf-8
- ai_challenger_oqmrc_testa.json
```json
{"url": "http://gsrb.gansudaily.com.cn/system/2009/08/23/011235562.shtml", 
"query": "武威的公交卡古浪能不能用", 
"query_id": 280001, 
"alternatives": "能|不能|无法确定", 
"passage": "武威公交一体化纪实 10家运输公司中标经营包括凉州区、古浪、民勤、天祝在内的城乡公交线路。经过收编、整合、更新，开通城乡公交客运班线23条，统一投放80辆高档次客运车辆，由运输公司统一管理。实际上，运营在这些线路的新型双开门公交车的标准、设施已远远超过城区公交车。武威运管部门通过市场竞争和行业引导，建立退出机制，规范经营行为，提升服务质量。 　　去年11月下旬，武威市区至古浪县城和凉州区50公里范围内的乡镇全部开通城乡公交，凉州区28个乡镇300个行政村更是全部覆盖城乡公交，率先实现“乡乡通公交，村村通客车”。这些城乡公交定时、定班、定点、定线，城乡公交均等化延伸到农民的家门口。“乡村小公交起到了穿针引线、走村串巷的功能。”沈兴国说。"}
```
* 10000 dict items
- ai_challenger_oqmrc_trainingset.json
```json
{
"url": "http://iask.sina.com.cn/key/5a73101384ae262303cef1ab.html", 
"alternatives": "无法确定|是|不是", 
"passage": "孩子是父母的一面镜子，由于儿童的世界观尚未形成，他们的模仿带有很大的盲目性，所以还是父母带好。除非万不得已，绝对不能把上早教课等教育问题交给保姆，她们负责生活起居就好了，树立孩子一生的良好习惯，家长们可千万不能大意。",
"query_id": 1, 
"query": "你的孩子是保姆带大的么",
"answer": "无法确定" 
}
```
* 250000 dict items
- ai_challenger_oqmrc_validationset_20180816.json
```json
{
"url": "http://www.120ask.com/question/65970789.htm", 
"alternatives": "能|不能|无法确定", 
"passage": "醋泡鸡蛋确实具有一定美白嫩化肌肤、提高皮肤亮度、祛斑的效果，因为白醋中含有的醋酸可以加速表皮新陈代谢、软化角质，鸡蛋清中的蛋白质可以嫩化肌肤，收缩毛孔的作用。", 
"query_id": 250002, 
"query": "醋泡鸡蛋真能去斑吗",
"answer": "能"
}
```
* 40000 dict items

### Data type
- data is shown as dict type, the dict key value
	- url, may not be used
	- alternatives
	- passage
	- query_id
	- query
	- answer \(not in the test set\)

### Data analysis
- every passage is within 500 words.
- 3 answers
- data has some problems
	- Yan text: 好次好次(•ؔʶ ˡ̲̮ ؔʶ)✧
	- answer with extra char/space/punctuation: 没有y|有|无法确定;没有 |右|无法确定
	- answer with the wrong words: 没有 |右|无法确定

### Tips for data preprocess
- for candidate answers/correct answers, delete extra char/space/punctuation, wrong words may not be discovered by manual work
- for passages, remove extra spaces and punctuation before and after the article
- token

### Result Submission
- txt file
	- queryid \t answertext, e.g., 100\t可以

### Evaluation metrics
- Accuracy = right questions/amount of testing questions
	

	

