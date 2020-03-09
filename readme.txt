本文数据来源：https://www.dcjingsai.com/common/cmpt/AI%E6%88%98%E7%96%AB%C2%B7%E5%B0%8F%E5%88%86%E5%AD%90%E6%88%90%E8%8D%AF%E5%B1%9E%E6%80%A7%E9%A2%84%E6%B5%8B%E5%A4%A7%E8%B5%9B_%E7%AB%9E%E8%B5%9B%E4%BF%A1%E6%81%AF.html

若不提供下载了可联邮箱297884974@qq.com


1. 原始train excel 展开为 train_fenlie.csv 经过特征选择 得到 train_fenlie1.csv
2. 利用 Baseline_train_fenlie1.ipynb ( 前1000例数据)构建pipeline "tpot_medical_pipeline_fenlie1.py"

3.运行pipeline文件 tpot_medical_pipeline_fenlie1.py 生成 模型 tpot_medical_pipeline_fenlie1.py

4. excel 调整 test_noLabel.csv  到 test.csv（与训练集格式相同）

5. test_medical.py 测试并生成提交文件 upload.csv 用excel删除多余列 

6. 结束
