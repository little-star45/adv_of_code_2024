// go run .
package main

import (
	"fmt"
	"strconv"
	"strings"
	"math"
	"slices"
)

func SplitStone(inputNumbers []float64) []float64{
	result := []float64{}
	slices.Sort(inputNumbers)

	for _,nb := range inputNumbers{
		
		if nb==0{
			result = append(result, 1)
		}else if nbLen := int(math.Log10(nb)+1); nbLen%2==0{
			halfNb := math.Pow10(int(nbLen/2))
			leftString, rightString := math.Modf(nb/halfNb)
			result = append(result, leftString, math.Round(rightString*halfNb))
		}else{
			result = append(result, nb*2024)
		}
	}

	return result
}

func ArrayToNumbers(inputStrings []string) []float64{
	result := []float64{}
	for _, value := range inputStrings{
		num, _ := strconv.ParseFloat(value, 64)
		result= append(result, num)
	}
	return result
}

func main(){

	blinkingTimes := 75
	puzzleInput := "4022724 951333 0 21633 5857 97 702 6"
	// puzzleInput := "125 17"
	splitPuzzleInput := strings.Split(puzzleInput, " ")
	intPuzzleInput := ArrayToNumbers(splitPuzzleInput)

	sumData := intPuzzleInput

	for i := 0; i < blinkingTimes; i++ {
		fmt.Printf(" %v/%v:\n",i+1, blinkingTimes)
		
		sumData = SplitStone(sumData)
		// fmt.Println(sumData)
	}

	fmt.Println("Sum results: ",len(sumData))
}