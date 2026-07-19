

##################################################
# Pandas Alıştırmalar
##################################################

import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################

df = sns.load_dataset("titanic")
print(df.head())

#########################################
# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################

print(df["sex"].value_counts())

#########################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#########################################

print(df.nunique())

#########################################
# Görev 4: pclass değişkeninin unique değerleri bulunuz.
#########################################

print(df["pclass"].nunique())


#########################################
# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################

print(df[["pclass", "parch"]].nunique())

#########################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
#########################################

print(df["embarked"].dtype)
df["embarked"] = df["embarked"].astype("category")
print(df["embarked"].dtype)

#########################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
#########################################

embarked_C = df[df["embarked"] == "C"]
print(embarked_C.head(10))

#########################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#########################################

embarked_not_S = df[df["embarked"] != "S"]
embarked_not_S.head(10)

#########################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################

task_9 = df[(df["age"] < 30) & (df["sex"] == "female")]
print(task_9.head())

#########################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
#########################################

task_10 = df[(df["fare"] > 500) | (df["age"] > 70)]
print(task_10.head(10))

#########################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################

print(df.isnull().sum())

#########################################
# Görev 12: who değişkenini dataframe'den düşürün.
#########################################

df.drop("who", axis=1, inplace=True)
print(df.columns)

#########################################
# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################
print(df["deck"].isnull().sum())
deck_mode = df["deck"].mode()[0]
print(deck_mode)

df["deck"] = df["deck"].fillna(deck_mode)
print(df["deck"].isnull().sum())

#########################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.
#########################################

print(df["age"].isnull().sum())

age_median  = df["age"].median()
print(age_median)

df["age"] = df["age"].fillna(age_median)
print(df["age"].isnull().sum())

#########################################
# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
#########################################

task_15 = df.groupby(["pclass", "age"]).agg({"survived": ["sum", "count", "mean"]})
print(task_15)

#########################################
# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
#########################################

def age_class(age):
    if age < 30:
        return 1
    else:
        return 0

df["age_flag"] = df["age"].apply(lambda x: age_class(x))
print(df[["age", "age_flag"]].head(10))

#########################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################

tips_df = sns.load_dataset("tips")
print(tips_df.head())

#########################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

time_stats = tips_df.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]})
print(time_stats)

#########################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

time_day_stats = tips_df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})
print(time_day_stats)

#########################################
# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
#########################################

lunch_female = tips_df[(tips_df["time"] == "Lunch") & (tips_df["sex"] == "female")]

task_20 = tips_df.groupby("day").agg({
    "total_bill": ["sum", "min", "max", "mean"],
    "tip": ["sum", "min", "max", "mean"]
})
print(task_20)
#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
#########################################

tips_df[(tips_df["size"] < 3) & (tips_df["total_bill"] > 10)].select_dtypes(include="number").mean()

#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################

tips_df = tips_df.copy()
tips_df["total_bill_tip_sum"] = tips_df["total_bill"] + tips_df["tip"]
print(tips_df.head())

#########################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################

top_30_tips = tips_df.sort_values("total_bill_tip_sum", ascending=False).head(30)
print(top_30_tips.head(15))

