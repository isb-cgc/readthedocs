**************
Visualizations
**************

The ISB-CGC web-app provides a variety of tools for visualizing the data associated with cohorts you have defined.
A visualization is a
collection of one or more plots and each plot is configurable to show relevant data that can be shared with others.

Create
######

You can create a new visualization from the user dashboard. Select the “Visualization” option from the “+ Create” menu.
This will prompt you to name the visualization and provide at least one cohort to start with. It will automatically
choose the last one you created. Click “Create Visualization”.

Save
####

Use the “Save Visualizations” option in the top right menu. It will save the visualization and all plots in their
current configuration. It will not save any selections that have been made within plots.

Delete
######

**From User Dashboard**
Select the visualizations that you wish to delete using the checkboxes next to the visualization. When one or more are
selected, the delete button will be active and you can then proceed to deleting them.

**From Visualization**
If you are viewing a visualization you created, then you can delete the cohort from the top right menu option.

Copy
####

Copying a visualization can only be done from the visualization you want to copy.

When you are looking at the visualization you wish to copy, select the “Make A Copy” item from the top right menu.

This will take you to your copy of the visualization.

Add Plot
########

To add a plot to a visualization, select the “Add a Plot” item in the top right menu.

This will append a new plot section to your visualization with the default plot of an age histogram for the All TCGA
Data Cohort.

Delete Plot
###########

To delete a plot from a visualization, select the “Trash” icon in the top right corner of the plot panel you wish to
remove.

Plot Comments
#############

To open the comments section for a particular plot, select the “Comment” icon in the top right corner of the plot panel.
This will cause the comment sidebar to appear from the right side of the window.

All previous comments will be displayed with the most recent on the bottom.

To add a new comment, type in your comment in the text box at the bottom of the panel and click the “Comment” button.
You should see your comment appear at the bottom of the list of comments.

Edit Plot
#########

To change the settings of a plot, select the “Edit” icon in the top right corner of the plot panel. This will cause the
Plot Setting panel to open.

Selecting new Feature(s)
========================

When you click on the edit icon next to the feature you would like to change (i.e. “X Axis Feature”, “Y Axis Feature”),
you will be taken to the feature selection panel.
Here you must first specify the datatype of the feature you would like to plot. Each datatype requires a different set
of parameters to narrow down the feature that can be used in the plot.

* Clinical
    * Single autocomplete textbox. This input searches through the names of the all the clinical features available.
* Gene Expression
    * Gene Filter: filters down the plot-able features by a specific gene. This is an autocomplete search field for a gene name.
    * Platform Filter: filters down the plot-able features by platforms.
    * Center Filter: filters down the plot-able features by processing center.
    * Select Feature: provides the filtered down list of plot-able features to select from based on selected filters.
* miRNA
    * miRNA Name Filter: filters down the plot-able features by a specific miRNA. This is an autocomplete search field for a miRNA name.
    * Platform Filter: filters down the plot-able features by platforms.
    * Value Filter: filters down the plot-able features by value.
    * Select Feature: provides the filtered down list of plot-able features to select from based on selected filters.
* Methylation
    * Gene Filter: filters down the plot-able features by a specific gene. This is an autocomplete search field for a gene name.
    * CpG Probe Filter: filters down the plot-able features by a specific CpG Probe. This is an autocomplete search field for a particular probe.
    * Platform Filter: filters down the plot-able features by platforms.
    * Gene Region Filter: filters down the plot-able features by specific gene regions.
    * CpG Island region Filter: filters down the plot-able features by CpG Island region.
    * Select Feature: provides the filtered down list of plot-able features to select from based on selected filters.
* Copy Number
    * Gene Filter: filters down the plot-able features by a specific gene. This is an autocomplete search field for a gene name.
    * Value Filter: filters down the plot-able features by value
    * Select Feature: provides the filtered down list of plot-able features to select from based on selected filters.
* Protein
    * Gene Filter: filters down the plot-able features by a specific gene. This is an autocomplete search field for a gene name.
    * Protein Filter: filters down the plot-able features by protein. This is an autocomplete search field for a protein name.
    * Select Feature: provides the filtered down list of plot-able features to select from based on selected filters.
* Mutation
    * Gene Filter: filters down the plot-able features by a specific gene. This is an autocomplete search field for a gene name.
    * Value Filter: filters down the plot-able features by mutation value.
* Select Feature: provides the filtered list of plot-able features to select from based on selected filters.
* Swap Values: This button allows you to instantly swap the features on the X and Y Axes without having to re-select each feature individually.
* Color By Cohort: This checkbox will override any feature that is in the Color By Feature. It will use the cohorts provided as the legend and Color By Feature.
* Cohorts: This is where you can select one or more cohorts to plot at one time.

To add a cohort, select the “+ Cohort” option underneath the currently selected list of cohorts. This will take you to
the cohorts listing panel where you can select a cohort from the list, or use the autocomplete textbox to search in
their list of cohorts.

When all the settings have been set, you can click “Update Plot” to regenerate the plot with the new settings.

Pairwise Statistical Test
#########################

Each pair of features selected for a plot will be tested for statistical significance, and the results will be
displayed beneath the plot.

