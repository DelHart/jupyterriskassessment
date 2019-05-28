# jupyterriskassessment
A set of Jupyter Notebooks for teaching risk assessment.

Threat Scenario data is stored in the database.  Although the
notebooks are editable, you must use the widget buttons within the
notebooks to save the data.  Saving the notebook will not save the
data.

Notebooks:

  org.ipynb
      edit data about the organization, including the mission,
      assets, and controls.

  triage.ipynb
      add and edit threats using a qualitative view
      recommended for initial work, but other notebooks should be used
      later

  qualitative dashboard.ipynb
      dashboard showing a summary of current threat scenarios and sources
      uses a qualitative perspective on the data

  basic.ipynb
      intermediate level threat editor that allows finer grain adjustment of
      threat parameters

  basic dashboard.ipynb
      display threat scenarios at an intermediate level of detail

  detailed.ipynb
      editor that allows adjustment of probability distributions associated
      with a threat.  It also has a simulator to estimate the Expected Annual
      Loss.

  quantitative dashboard.ipynb
      display summary of threat scenarios including numeric parameters

  report.ipynb
      Generate a report of all threat scenarios suitable for printing

Other files:
   distributions.ipynb - a notebook to explore different probabiliy distributions
   qual.py - helper functions and data
   quant.py - helper functions and data

  

Recommended order:

1. org - identify the context for the risk assessment
2. triage - enter the threat scenarios under consideration at a low level of detail
3. basic or detailed ( depending on the type of analysis being done)
4. report
