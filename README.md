# Python-Resize-Image

![Python-Resize-Image](https://github.com/blyamur/Python-Resize-Image/blob/main/hello.jpg)

I am sharing a Python script for Windows to resize images to a specified size. I did it according to my tasks, so the functionality has some limitations. The script is available on Github, and you can use it in your projects and change the functionality to suit your tasks and needs.

The script itself does not represent anything over and above outstanding and there is nothing new in it, except that it basically has an interface (GUI) with one button. You can use the script either through the Windows command line (CMD), or by compiling the script into an EXE file, for example, through the pyinstaller.


>Делюсь скриптом на Python под Windows для изменения размера изображений, до указанного размера. Делал под свои задачи, поэтому функционал имеет некоторую ограниченность. Скрипт доступен на Github, и вы можете использовать его в своих проектах и изменять функционал под ваши задачи и потребности.

>Сам скрипт не представляет ничего сверх выдающегося и в нем нет ничего нового, кроме того, что в нем принципиально сделан интерфейс (GUI) с одной кнопкой. Использовать скрипт можно как через командную строку Windows (CMD), так и собрав скрипт в EXE файл, например через pyinstaller.


```
pyinstaller resizer.py --noconsole --onefile --icon=resizer.ico
```


The script comes with icons in the .ico format and the source in the .svg format, so if necessary, you don't need to look for anything separately, everything is already there, and the code has been commented whenever possible to make it clearer and more convenient. 

>В комплекте со скриптом, идет и иконки в формате .ico и исходник в формате .svg, так что при необходимости, ничего отдельно вам искать не надо, все уже есть, а код по возможности прокомментировал, чтобы было понятнее и удобнее.


General view of the file selection window
> Общий вид окна выбора файла
![Python-Resize-Image](https://github.com/blyamur/Python-Resize-Image/blob/main/example%20window.jpg)

After starting the script, a window opens with a single button, by clicking on which you will be prompted to select an image file. After you select the desired image, the script checks the file extension, separates the path to the file from its name and extension. Then the file resolution is changed to the sizes specified in the settings, after which a new file name is generated, which is added to the existing one, after which the image is saved in the same folder where the original is stored, and you receive a notification about the successful resizing. The new file is in the same folder as the original.

At the same time, the original remains intact, and the new name allows you to quickly find a new file among the existing ones. A random combination of characters and the new file size are appended to the current file name. For example, the original name of the image is 1622448937128.jpg, the new name will be in the spirit: uYKOyFJdWbjUqkxl_1622448937128_1920.jpg

All settings, of which there are only two items, are available in lines 15 and 16.

> После запуска скрипта, открывается окно с одной единственной кнопкой, нажав на которую вам будет предложено выбрать файл изображения. После выбора вами нужного изображения, скрипт проверяет расширение файла, разделяет путь к файлу от его названия и расширения. Затем идет изменение разрешения файла, до указанных в настройках размеров, после чего генерируется новое название файла, которое добавляется к имеющемуся, после чего изображение сохраняется в той же папке, где и хранится оригинал, а вы получается уведомление об успешном изменении размеров. Новый файл лежит в той же папке, что и оригинал.

> Оригинал при этом остается нетронутым, а новое название позволяет быстрее найти новый файл среди уже имеющихся. К текущему названию файла, добавляется случайная комбинация символов и новый размер файла. Например оригинальное название изображения 1622448937128.jpg, новое название будет в духе: uYKOyFJdWbjUqkxl_1622448937128_1920.jpg

> Все настройки, которых всего два пункта, доступны в строках 15 и 16.

In the script, you can manually set the parameters:
> В скрипте можно вручную задать следующие параметры

```
factor = 2 # степень улучшения изображения
basewidth = 1920 # до какого размеры уменьшаем
```

You can play with each of the items, they are selected individually for your needs. You can set the required size "basewidth", to which you need to reduce the images and save the changes, playing with the "factor" line, increasing or decreasing the values, and then checking at which of the values ​​you specified, the image quality after processing is completely satisfactory for you. And you can leave everything as it is.

The script was primarily made for myself and according to my needs, therefore it is published in a state as is (AS IS). If necessary, you can change it for yourself, for example, add a multi-selection of files, add options for choosing the size and degree of improvement, compression ratio, the ability to select a save location, renaming options.

>С каждым из пунктов можно поиграть, они подбираются индивидуально под ваши потребности. Можно выставить необходимый размер «basewidth», до которого необходимо уменьшать изображения и сохранив изменения играя со строкой «factor» увеличивая или уменьшая значения, а затем проверяя при каком из указанных вами значений, качество изображения после обработки, вас полностью удовлетворяет. А можно оставить все как есть.

>Скрипт в первую очередь делался для себя и под свои нужды, поэтому публикуется в состоянии как есть (AS IS). Вы при необходимости можете изменить его под себя, например добавить мультивыбор файлов, добавить опции выбора размера и степени улучшения, степень сжатия, возможность выбора места сохранения, варианты переименования.


This script does not claim to be original or correct. It is provided as is, the main thing is that it completely allows you to solve the tasks.
> Данный скрипт не претендует на оригинальность и правильность. Предоставляется как есть, главное он вполне позволяет решать поставленные задачи.

### Copyrights and Licenses
Not for commercial use.

© 2022

 [Version with more features - Feodora](https://github.com/blyamur/Feodora/)


<!--
### Did you find this useful?!
> Вы нашли это  полезным ?!

Happy to hear that :) *If You want to help me, you can buy me a cup of cup of coffee ( [yoomoney](https://yoomoney.ru/to/41001158104834) or [PayPal](https://paypal.me/enkonu) or [ko-fi](https://ko-fi.com/W7W460SQ3) )*

> Рад это слышать :) Если вы хотите мне помочь, вы можете угостить меня чашкой кофе
 -->

*Thanks for reading :heart_eyes_cat:*
> Спасибо за чтение!
