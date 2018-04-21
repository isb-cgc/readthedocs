Radiology Viewer
================
Radiology images are viewed in an Osimis Web Viewer, a plug-in to the Orthanc image server (Orthanc). The ISB_CGC web application uses an instance of Orthanc to manage radiology files for the purpose of viewing. Currently only DICOM formatted files from TCGA samples are available for viewing. It may be helpful to understand the `DICOM Model of the Real World <http://dicom.nema.org/medical/dicom/current/output/html/part03.html#chapter_7>`_. 

An instance the radiology viewer is opened in a new tab when a DICOM study is selected in the ISB-CGC web application `File Browser page`_. All the DICOM series which comprise the selected study are shown as thumbnail images on the left side of the page. Note that it can take several seconds for these thumnails to appear.

.. _File Browser page: https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/webapp/Saved-Cohorts.html#view-file-browser-page

By default, the thumbnails are laid out in a grid pattern. This can be changed to a list display by clicking on the **List Display** button |list| above the thumbnails. To the lower right of each thumbnail is a small blue circle in which is displayed the number of DICOM instances which comprise the corresponding DICOM series. In addition, when your cursor hovers over a thumbnail, the viewer cycles through those instances. (Note these low resolution images are loaded in the background and may not be available for cycling immediately after the viewer window opens.)

.. |list| image:: OsimisList.png

To view a larger rendering of a series, drag its thumbnail into the main window. The first instance of the series is immediately displayed to fill the main window. At the same time, you will notice a grid at the bottom of the main window, which is comprised of a series of rectangles corresponding to the instances in the series. The color of the tabs indicates the following:

* Black: The corresponsing instance has not been loaded
* Red: A reduced resolution image of the instance is being displayed
* Green: The full resolution image of the instance is being displayed

Typically, the viewer loads reduced resolution instance for all series as quickly as possible. It loads full resolution images only when a series is dragged into the main window.

When instance images are loaded, you can scroll through the instances using your mouse's thumbwheel or equvalent. As you scroll, the grid at the bottom of the screen highlights the instance currently being displayed. Clicking on a rectangle in the grid causes the corresponding instance to be displayed. Finally, the controls in the lower left corner of the main window enable you to single step forward or back through the series, and to cycle throught series repeatedly. A frame rate slider pops up when you hover over the play button. 

A set of buttons above the viewport provides a range of functions. 

.. image:: OsimisViewportButtons.png
  :align: center

The **Layout** button |layout| enables subdividing the viewport for the simultaneous display of one, two or four series. Drag a series into any of the subviewports to display it. Clicking in a subviewport gives it focus for mousewheel and cursor drag operations.

.. |layout| image:: OsimisLayout.png

Of the remaining buttons, some are modal, changing the effect of the cursor drag function. A blue line underscores the currently selected mode. Other buttons immediately perform some operation on the subviewport that has focus.

* The **Invert Color** button |invert| immediately inverts the colors of the subviewport with focus.

.. |invert| image:: OsimisInvertColor.png
* The **Zoom** button |zoom| is modal. When selected, dragging the cursor with mouse button depressed expands or contracts the image in the subviewport having focus. Expansion/contraction is around the cursor position when dragging begins.

.. |zoom| image:: OsimisZoom.png
* The **Pan** button |pan| is modal. When selected, dragging the cursor with mouse button depressed causes panning of the image in the subviewport having focus. 

.. |pan| image:: OsimisPanning.png
* The **Presets** button |presets| is modal. Hovering the cursor over the button displays a list of presets, one of which can be selected by clicking on it. The selected preset does something with contrast.

.. |presets| image:: OsimisPresets.png
* The **Magnifying Glass** button |glass| is modal. Hovering the cursor over the button displays a pop-up containing two sliders that control the magnification level and size of a virtual magnifying glass. When selected, dragging the cursor with mouse button depressed opens a virtual magnifying glass that displays a magnified rendering of the underlying image in the region of the cursor.

.. |glass| image:: OsimisGlass.png

* The **Length Measurement** button |len| is modal. When selected, the distance in physical units between two points in an image can be measured. To perform a measurement, click the mouse button once with the cursor over some point of interest, and then again over a second point of interest. Alternatively, depress and hold the mouse button while the cursor is over the first point of interest, then release the mouse button while the cursor is over the send point of interest. A line joining the two points and its length are displayed. The line will scale if the image is zoomed in or out.

  A measurement line can be moved by clicking on it and dragging. To remove a measurement line, drag an endpoint outside of the (sub)viewport.
 
  A length measurement is only visible on the instance on which it was made. There is currently no support for saving length measurements.

.. |len| image:: OsimisLength.png
* The **Angle Measurement** button |ang| is modal. When selected, the angle between two lines in an image can be measured. To perform a measurement, click on a point of interest in an image. A pair of lines are displayed. Drag the end points of the lines as needed to form the angle to be measured. The angle between the line is displayed continuously as any endpoint is dragged.
  
  An angle measurement can be moved by clicking on one of the lines and dragging it while holding down the mouse button. To remove an angle measurement, drag an endpoint outside of the (sub)viewport.
  
  An angle measurement is only visible on the instance on which it was made. There is currently no support for saving angle measurements.  

.. |ang| image:: OsimisAngle.png
* The **Pixel Probe** button |probe| is modal. When selected, clicking on a point in an instance displays a circle at the probe point, the X and Y location of the pixel relative to the top left corner of the instance, and the intensity or color of the selected pixel. The intensity of monochrome instance pixels is specified in both SP and MO coordinates. The value of color instance pixels is specified in RGB coordinates.

  An pixel probe can be moved by clicking on the probe indicator and dragging it while hold down the mouse button. To remove a probe, drag it outside of the (sub)viewport.

  A pixel probe is only visible on the instance on which it was made. There is currently no support for saving pixel probes.  

.. |probe| image:: OsimisPixelProbe.png
* The **Elliptical ROI** button |eROI| is modal. When selected, click and drag one of the small circles to configure an ellipse around a region of interest. You can drag either of the control circles for this purpose. The area in pixels of the ellipse is displayed near the ellipse. On monotone instances, the mean and standard deviation of the intensities of the pixels within the ellipse are also displayed. 
  
  An ellipse can be moved by clicking on the border of the ellipse and dragging it while holding down the mouse button. To remove an ellipse, drag one of its control points outside of the (sub)viewport.

  An elliptical ROI  is only visible on the instance on which it was made. There is currently no support for saving elliptical ROIs.
  
.. |eROI| image:: OsimisEllipticalROI.png



  

  
  
