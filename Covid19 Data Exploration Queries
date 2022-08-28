-- A preview into the covid19 deaths dataset
SELECT *
FROM Covid19.Covid19_Deaths
LIMIT 100

-- Finding the number of cases,deaths against the total population per each continent.
-- It shows death likehood per each case in each continent.
SELECT 
continent,SUM(total_cases)AS Total_Cases,SUM(total_deaths) AS Total_Deaths,SUM(population) AS Total_Population, (SUM(total_deaths)/SUM(total_cases)*100) AS Death_Percentage
FROM 
Covid19.Covid19_Deaths
WHERE 
continent NOT IN ('International','World','European Union')
GROUP BY continent
ORDER BY 2,3 DESC

-- Finding the aged population per each country
SELECT 
location,SUM(population) AS Total_population,(aged_65_older* population) AS Aged_65, (aged_70_older* population) AS Aged_70, ((aged_65_older* population) + (aged_70_older* population)) AS Aged_Population, ((aged_65_older* population) + (aged_70_older* population))/ population AS Aged_Population_Percentage
FROM Covid19.Covid19_Deaths
WHERE location NOT IN ('Oceania','Africa','South America','Asia','North America','Europe','International','World','European Union')
GROUP BY location,Aged_65,Aged_70,Aged_Population,Aged_Population_Percentage
ORDER BY 6 DESC

-- Finding the countries with highest cases per population
SELECT 
location AS Country,SUM(total_cases)AS Total_Cases,SUM(population) AS Total_Population,
FROM 
Covid19.Covid19_Deaths
WHERE location NOT IN ('Oceania','Africa','South America','Asia','North America','Europe','International','World','European Union')
GROUP BY
location
ORDER BY 2 DESC,3 DESC

-- A preview into the covid19 vaccinations dataset
SELECT *
FROM Covid19.Covid19_Vaccinations
LIMIT 100

-- Finding the total vaccination against the total population per country
SELECT 
Covid19_Deaths.continent AS Continent,Covid19_Deaths.location AS Country,SUM(Covid19_Deaths.population) AS Total_population,SUM(Covid19_Vaccinations.total_vaccinations) AS Total_Vaccinations
FROM 
Covid19.Covid19_Deaths
JOIN 
Covid19.Covid19_Vaccinations
ON 
Covid19_Deaths.location = Covid19_Vaccinations.location
WHERE 
Covid19_Deaths.location NOT IN ('Oceania','Africa','South America','Asia','North America','Europe','International','World','European Union')
GROUP BY
Covid19_Deaths.location,Covid19_Deaths.continent
ORDER BY
3 DESC,4 DESC

--Finding the running totals of vaccinations for each country with respective vaccination days
SELECT 
Covid19_Deaths.continent AS Continent,Covid19_Deaths.location AS Country,Covid19_Deaths.population AS Total_population,Covid19_Vaccinations.total_vaccinations AS Total_Vaccinations, Covid19_Deaths.date, SUM(Covid19_Vaccinations.total_vaccinations) OVER (PARTITION BY Covid19_Deaths.location ORDER BY Covid19_Deaths.location,Covid19_Deaths.date) AS Running_Vaccination_Total
FROM 
Covid19.Covid19_Deaths
JOIN 
Covid19.Covid19_Vaccinations
ON 
Covid19_Deaths.location = Covid19_Vaccinations.location  AND Covid19_Deaths.date = Covid19_Vaccinations.date
WHERE 
Covid19_Deaths.location NOT IN ('Oceania','Africa','South America','Asia','North America','Europe','International','World','European Union')
ORDER BY
3, 4

-- Using CTE to find the proportion of vaccinated individuals per country

WITH PopVac AS (SELECT 
Covid19_Deaths.continent AS Continent,Covid19_Deaths.location AS Country,Covid19_Deaths.population AS Total_population,Covid19_Vaccinations.total_vaccinations AS Total_Vaccinations, Covid19_Deaths.date, SUM(CAST(Covid19_Vaccinations.total_vaccinations AS int64)) OVER (PARTITION BY Covid19_Deaths.location ORDER BY Covid19_Deaths.location,Covid19_Deaths.date) AS Running_Vaccination_Total
FROM 
Covid19.Covid19_Deaths
JOIN 
Covid19.Covid19_Vaccinations
ON 
Covid19_Deaths.location = Covid19_Vaccinations.location  AND Covid19_Deaths.date = Covid19_Vaccinations.date
WHERE 
Covid19_Deaths.location NOT IN ('Oceania','Africa','South America','Asia','North America','Europe','International','World','European Union')
ORDER BY
2, 3)

SELECT *, (Running_Vaccination_Total/Total_population * 100) AS Running_Vaccination_Percentage
FROM PopVac
