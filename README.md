# ML-model-training
Модель для сайта <code>[**Geolin 2.0**](https://github.com/M3100Team/firstlab#readme)</code>, классифицирующая изображения на фотографии с дз по линейной алгебре и любые другие фотографии. Итоговая модель должна по принимаемому объекту PIL.Image выдовать вероятность того, что фотография **является** рукописным дз по линейной алгебре.

# Описание файлов:
* **data_generation.py** - генерация картинок для датасета.
* **raw_data** - папка с сырыми данными, взятыми из интернета(<code>[**математические символы**](https://www.kaggle.com/xainano/handwrittenmathsymbols)</code>,<code>[**ещё математические символы**](https://www.kaggle.com/clarencezhao/handwritten-math-symbol-dataset)</code> , <code>[**случайные картинки нелинала**](https://www.kaggle.com/prasunroy/natural-images)</code>)
* **dataset_false** - сгенерированный датасет нелинала
* **dataset_true** - сгенерированный датасет линала
* **training.ipynb** - ноутбук с обучением модели
