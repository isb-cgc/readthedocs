Radiology Viewer
================
Radiology images are viewed in an Osimis Web Viewer, a plug-in to the Orthanc image server (Orthanc). The ISB_CGC web application uses an instance of Orthanc to manage radiology files for the purpose of viewing. Currently only DICOM formatted files from TCGA samples are available for viewing. It may be helpful to understand the `DICOM Model of the Real World <http://dicom.nema.org/medical/dicom/current/output/html/part03.html#chapter_7>`_. 

An instance the radiology viewer is opened in a new tab when a DICOM study is selected in the ISB-CGC web application `File Browser page`_. All the DICOM series which comprise the selected study are shown as thumbnail images on the left side of the page. By default, the thumbnails are laid out in a grid pattern. This can be changed a list display by clicking on the list icon above the thumbnails. To the lower right of each thumbnail is a small blue circle in which is displayed the number of DICOM instances which comprise the corresponding DICOM series. In addition, when your cursor hovers over a thumbnail, the viewer cycles through those instances. (Note these low resolution images are loaded in the background and may not be available for cycling immediately after the viewer window opens.)

.. _File Browser page: https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/webapp/Saved-Cohorts.html#view-file-browser-page

To view a larger rendering of a series, drag its thumbnail into the main window. The first instance of the series is immediately displayed to fill the main window. At the same time, you will notice a grid at the bottom of the main window, which is comprised of a series of rectangles corresponding to the instances in the series. The color of the tabs indicates the following:

* Black: The corresponsing instance has not been loaded
* Red: A reduced resolution image of the instance is being displayed
* Green: The full resolution image of the instance is being displayed

Typically, the viewer loads reduced resolution instance for all series as quickly as possible. It loads full resolution images only when a series is dragged into the main window.

When instance images are loaded, you can scroll through the instances using your mouse's thumbwheel or equvalent. As you scroll, the grid at the bottom of the screen highlights the instance currently being displayed. Clicking on a rectangle in the grid causes the corresponding instance to be displayed. Finally, the controls in the lower left corner of the main window enable you to single step forward or back through the series, and to cycle throught series repeatedly. A frame rate slider pops up when you hover over the play button. 

A set of buttons above the viewport provides a range of functions. 

.. image:: OsimisViewportButtons.png
  :align: center

The **Layout Button** |layout| enables subdividing the viewport for the simultaneous display of one, two or four series. Drag a series into any of the subviewports to display it. Clicking in a subviewport gives it focus for mousewheel and cursor drag operations.

.. |layout| image:: OsimisLayout.png

Of the remaining buttons, some are modal, changing the effect of the cursor drag function. A blue line underscores the currently selected mode. Other buttons immediately perform some operation on the subviewport that has focus.

* The **Invert Color Button** |invert| immediately inverts the colors of the subviewport with focus.

.. |invert| image:: OsimisInvertColor.png
* The **Zoom Button** |zoom| is modal. When selected, dragging the cursor expands or contracts the image in the subviewport having focus. Expansion/contraction is around the cursor position when dragging begins.

.. |zoom| image:: OsimisZoom.png
* The **Pan Button** |pan| is modal. When selected, dragging the cursor causes panning of the image in the subviewport having focus. 

.. |pan| image:: OsimisPanning.png
* The **Presets Button** |presets| is modal. Hovering the cursor over the button displays a list of presets, one of which can be selected by clicking on it. The selected preset does something with contrast.

.. |presets| image:: OsimisPresets.png





|ellip| support additional operations.

.. |ellip| image:: OsimisEllipticalROI.png
  :align: top
  

  
  
