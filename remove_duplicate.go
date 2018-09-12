func RemoveStringDuplicate(strSlice []string) []string {
	if len(strSlice) == 0 {
		return strSlice
	}
	strMap := make(map[string]bool)
	for _, d := range strSlice {
		strMap[d] = true
	}
	result := make([]string, len(strMap))
	i := 0
	for k, _ := range strMap {
		result[i] = k
		i++
	}
	return result
}
