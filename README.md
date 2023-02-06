# IXL OpenAI Solver
AI or math formulas automating doing IXL problems.

Currently the only lessons coded are Q2 and Q3 (partially)

This uses Selenium for automation and Open AI or direct math to compute the problems. Some errors that happen often are timing issues, sometimes the predicted onload time (5s) is too quick, and Selenium tries to find and click the next button before it appears. When this happens just restart, or change the time.sleep(x) value to a higher number. Other issues is whenever IXL changes to a different type of problem, and the AI or selenium can't compute the problem or click the buttons.

OpenAI: https://openai.com/

Selenium (python lib): https://selenium-python.readthedocs.io/

Selenium GitHub: https://github.com/baijum/selenium-python

IXL: https://ixl.com
