---
title: "agriHanda: an Agricultural Disaster Risk Web App"
description: "I discuss the web app that I created, which won two awards in the Project SPARTA PH Open Data Challenge for Butuan City.
layout: post
toc: true
comments: true
image: images/markdown-images/agriHanda/sample choropleth map.png
hide: true
search_exclude: true
categories: [streamlit, pandas, geopandas, altair, git]
---

![](https://miguelahg.github.io/mahg-data-science/images/markdown-images/agriHanda/agriHanda-choropleth-map.png)

<center><i>The 'Map of Butuan City' feature of agriHanda.</i></center>

</br>

On November 12, 2021, the Project SPARTA Recognition Ceremony took place. In the Open Data Challenge for Butuan City, my team was awarded as Second Placer and Best in Ingenious Solution.

In this post, I will talk about the web app, my experience participating in the competition, my web app's strengths and points for improvement, and the data science skills that I honed along the way.

# The Web App

First, I will give a brief introduction to the web app, agriHanda. The \"agri\" part of the name refers to agriculture, whereas the \"Handa\" part is a Tagalog or Bisaya word for \"prepared\". Thus, the title encapsulates the goal of the app to help the LGU prepare for natural hazards which may pose a threat to the city's agriculture industry.

Specifically, the app is a dashboard since it focuses on creating helpful visualizations of data. It uses data about the vulnerability of Butuan City's crops, fisheries, and livestock viz-a-viz drought, flooding, rain-induced landslide, sea level rise, and storm surge. 

The app has three main features. The \"Map of Butuan City\" feature shows a choropleth map. This means that the user can select a variable about agricultural disaster risk, and the colors of the barangays change based on the value of this variable. For example, it can show which general areas have a high vulnerability score of crops against flooding. The \"Barangay Data Summary\" feature presents tables and histograms that summarize the disaster risk scores of a chosen barangay. Lastly, the \"Graphing Tool\" feature allows the user to create a custom chart using one or two disaster risk variables.

For more information, you can watch our short four-minute pitch presentation about the app.

**Put video here.**

To try out the app yourself, visit this link: [bit.ly/agriHanda](https://bit.ly/agriHanda)

For more technical details about the project, visit the documentation through this link: [agriHanda - Agricultural Disaster Risk App](https://docs.google.com/document/d/1feKAvHEzJG2PmKtZrXvsGHOJL4c-kaTc4b_W_fHP-68/edit?usp=sharing)

The recognition ceremony can also be watched here: [SPARTA Recognition Ceremony](https://www.facebook.com/watch/live/?ref=watch_permalink&v=402923554635179)

# The Competition Experience

In June 2021, I read that there was an upcoming local competition in data science and analytics. This was the Project SPARTA Open Data Challenge, which was organized by the Development Academy of the Philippines and DOST-PCIEERD. The [Sparta Portal](https://sparta.dap.edu.ph/opendata/) provided open data about Butuan City, which is the \"commercial, industrial and administrative center\" of the Caraga region (\"Butuan City\", n.d.). Participants could then use this data to create cleaned datasets, datablogs, data journalism pieces, research papers, dashboards, predictive models, software applications, or visual storytelling pieces.

While I looked through the provided datasets, I noticed that most of these were about vulnerability risk assessments of various aspects of the city against natural hazards. These aspects included agriculture, roads, bridges, schools, and others. Thus, out of the five available challenges in the competition, I chose to join the one entitled, \"Approach to innovations and innovative techniques to food sufficiency using data and technology.\" I would address potential risks to Butuan City's food sufficiency by focusing on the data about crops, fisheries, and livestock.

Thus, I formed a team with three of my schoolmates (Fiona Jao, Lorenzo Layug, and Yuri Dolorfino), and we entered the competition as the \"Datos Puti\" team. As team leader, I wrote planning documents, delegate tasks, set deadlines, and did the programming work. My members mainly helped with the first phase of the project, data cleaning.

We divided the data files amongst ourselves, then we manually looked through each row and column to note missing or erroneous values. Based on our notes, I fixed some of the errors and wrote a Python program to automate the rest of the cleaning process. In the end, all of the data was combined into a single large dataset, which was organized into a hierarchy for ease of navigation. We would later submit this cleaned dataset alongside the web app so that government researchers could analyze it directly without having to use our app.

Then, I programmed the agriHanda web app. The process was difficult, as I had to work on the app almost every night, balance it with my academic responsibilities, address seemingly unsolvable bugs. In the end, however, I was able to implement all three features of the app and submit it on time.

Finally, during the recognition ceremony in November, we were given the \"Second Placer\" and \"Best in Ingenious Solution\" awards. I was proud of this because this was the first data science competition that I had ever joined. Furthermore, despite being a senior high school student at the time, I was able to perform well against the other eleven competing teams, most of whom were from the college and professional levels. 

# Reflection

# Data Science Skills