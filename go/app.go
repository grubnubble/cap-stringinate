package main

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

var seen_strings map[string]int = make(map[string]int)

type StringData struct {
	Input  string `param:"input" query:"input" form:"input" json:"input" xml:"input"`
	Length int    `json:"length"`
}

type StatsData struct {
	Inputs map[string]int `json:"inputs"`
}

func remember(input string) {
	if seen_strings[input] == 0 {
		seen_strings[input] = 1
	} else {
		seen_strings[input] += 1
	}
}

func stringinate(c echo.Context) (err error) {
	request_data := new(StringData)
	if err = c.Bind(request_data); err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, err.Error())
	}
	remember(request_data.Input)
	response_data := StringData{request_data.Input, len(request_data.Input)}
	return c.JSON(http.StatusOK, response_data)
}

func stats(c echo.Context) (err error) {
	return c.JSON(http.StatusOK, StatsData{seen_strings})
}

func main() {
	e := echo.New()

	e.GET("/", func(c echo.Context) error {
		return c.HTML(http.StatusOK, `
			<pre>
			Welcome to the Stringinator 3000 for all of your string manipulation needs.
			GET / - You're already here!
			POST /stringinate - Get all of the info you've ever wanted about a string. Takes JSON of the following form: {"input":"your-string-goes-here"}
			GET /stats - Get statistics about all strings the server has seen, including the longest and most popular strings.
			</pre>
		`)
	})

	e.POST("/stringinate", stringinate)
	e.GET("/stringinate", stringinate)
	e.GET("/stats", stats)
	e.Logger.Fatal(e.Start(":1323"))
}
