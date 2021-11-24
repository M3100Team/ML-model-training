# ML-model-training
Модель для сайта <code>[**Geolin 2.0**](https://github.com/M3100Team/firstlab#readme)</code>, классифицирующая изображения на фотографии с дз по линейной алгебре и любые другие фотографии. Итоговая модель должна по принимаемому объекту PIL.Image выдовать вероятность того, что фотография **является** рукописным дз по линейной алгебре.

# Описание файлов:
* **data_generation.py** - генерация картинок для датасета.
* **raw_data** - папка с сырыми данными, взятыми из интернета(<code>[**математические символы**](https://www.kaggle.com/xainano/handwrittenmathsymbols)</code>,<code>[**ещё математические символы**](https://www.kaggle.com/clarencezhao/handwritten-math-symbol-dataset)</code> , <code>[**случайные картинки нелинала**](https://www.kaggle.com/prasunroy/natural-images)</code>)
* **dataset_false** - сгенерированный датасет нелинала
* **dataset_true** - сгенерированный датасет линала
* **training.ipynb** - ноутбук с обучением модели
* **test_false_easy** - папка с тестовыми картинками не дзшками, легко распознаваемыми моделью (котики, пейзажи, всякая дичь...)
* **test_false_hard** - папка с тестовыми картинками не дзшками, неоднозначно распознаваемыми моделью (дз по другим предметам, скрины веб сайтов, что-то похожее на лист бумаги...)
* **test_true** - папка с тестовыми картинками дзшками, собранными у рельных людей
* **model_test.ipynb** - ноутбук с тестом модели на реальных данных
