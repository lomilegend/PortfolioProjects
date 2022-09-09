-- A preview into the covid19 deaths dataset
SELECT *
FROM Covid19.Covid19_Deaths
LIMIT 100

-- Finding the number of highest monthly cases and deaths against the monthly mortality ratio per country.

SELECT 
continent,location,MAX(total_cases) AS Max_Cases,MAX(total_deaths) AS Max_Deaths,population AS Total_Population, (MAX(total_deaths)/MAX(total_cases)*100) AS Death_Percentage,DATE_TRUNC(date,MONTH) AS Month
FROM 
Covid19.Covid19_Deaths
WHERE 
location NOT IN ('Oceania','Africa','South America','Asia','North America','Europe','International','World','European Union')
GROUP BY continent,population,location,Month
ORDER BY 7 DESC

-- Finding the porportion of aged population per country
SELECT 
DISTINCT(location),population AS Total_population,((aged_65_older/100)* population) AS Aged_65_plus, ((aged_65_older/100)* population)/ population AS Aged_Population_Percentage
FROM Covid19.Covid19_Deaths
WHERE location NOT IN ('Oceania','Africa','South America','Asia','North America','Europe','International','World','European Union')
GROUP BY location,population,Aged_65_plus,Aged_Population_Percentage
ORDER BY 4 DESC

-- Finding the countries with highest cases and deaths per population
SELECT 
location AS Country,MAX(total_cases)AS Max_Cases,MAX(total_deaths) AS Max_Deaths,population AS Total_Population
FROM 
Covid19.Covid19_Deaths
WHERE location NOT IN ('Oceania','Africa','South America','Asia','North America','Europe','International','World','European Union')
GROUP BY
location,population
ORDER BY 2 DESC,3 DESC

-- Finding the total Cases against total deaths to show the likelihood of dying if you contract Covid19 in your country
SELECT location, date, total_cases,total_deaths, (total_deaths/total_cases)*100 as DeathPercentage
FROM 
Covid19.Covid19_Deaths
WHERE location NOT IN ('Oceania','Africa','South America','Asia','North America','Europe','International','World','European Union')
ORDER BY 1,2



-- Showing contintents with the highest death count per population
SELECT continent, MAX(CAST(Total_deaths as int)) AS Total_Death_Count
FROM 
Covid19.Covid19_Deaths
WHERE continent NOT IN ('International','World','European Union')
GROUP BY 1
ORDER BY 2 desc




-- A preview into the covid19 vaccinations dataset
SELECT *
FROM Covid19.Covid19_Vaccinations
LIMIT 100

-- Finding the total monthly vaccination against the total population per country
SELECT 
DISTINCT(Covid19_Deaths.location) AS Country,Covid19_Deaths.population AS Total_population,Covid19_Vaccinations.total_vaccinations AS Total_Vaccinations,DATE_TRUNC(Covid19_Vaccinations.date,MONTH) AS Month
FROM 
Covid19.Covid19_Deaths
JOIN 
Covid19.Covid19_Vaccinations
ON 
Covid19_Deaths.location = Covid19_Vaccinations.location
WHERE 
Covid19_Deaths.location NOT IN ('Oceania','Africa','South America','Asia','North America','Europe','International','World','European Union')
ORDER BY
2 DESC,3

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