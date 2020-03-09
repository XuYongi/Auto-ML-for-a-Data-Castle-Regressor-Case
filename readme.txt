1. 原始train excel 展开为 train_fenlie.csv 经过特征选择 得到 train_fenlie1.csv
2. 利用 Baseline_train_fenlie1.ipynb ( 前1000例数据)构建pipeline "tpot_medical_pipeline_fenlie1.py"

3.运行pipeline文件 tpot_medical_pipeline_fenlie1.py 生成 模型 tpot_medical_pipeline_fenlie1.py

4. excel 调整 test_noLabel.csv  到 test.csv（与训练集格式相同）

5. test_medical.py 测试并生成提交文件 upload.csv 用excel删除多余列 

6. 结束