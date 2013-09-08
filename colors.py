def list_of_colors(num):
    if num == 2:
        return ["#FFF7FB", "#3690C0"]
    if num == 3:
        return ["#ECE7F2", "#A6BDDB', textColor:'#333", "#2B8CBE"]
    if num == 4:
        return ["#F1EEF6", "#BDC9E1', textColor:'#333", "#74A9CF", "#0570B0"]
    if num == 5:
        return ["#F1EEF6", "#BDC9E1', textColor:'#333", "#74A9CF", "#2B8CBE", "#045A8D"]
    if num == 6:
        return ["#F1EEF6", "#D0D1E6', textColor:'#333", "#A6BDDB", "#74A9CF", "#2B8CBE", "#045A8D"]
    if num == 7:
        return ["#F1EEF6", "#D0D1E6', textColor:'#333", "#A6BDDB", "#74A9CF", "#3690C0", "#0570B0", "#034E7B"]
    if num == 8:
        return ["#FFF7FB", "#ECE7F2', textColor:'#333", "#D0D1E6", "#A6BDDB", "#74A9CF", "#3690C0", "#0570B0", "#034E7B"]
    if num == 9:
        return ["#FFF7FB", "#ECE7F2', textColor:'#333", "#D0D1E6", "#A6BDDB", "#74A9CF", "#3690C0", "#0570B0", "#045A8D", "#023858"]

def choose_color(num, total):
    return list_of_colors(total)[num - 1]