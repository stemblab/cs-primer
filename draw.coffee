window.drawing = ->
    
    return # disabled - replaced by png
    
    d = new Drawing id: "canvas", height: 250
    return unless d.canvas
                    
    mixer = d.circle {x: 300, y: 80, radius: 20, label: "$\\Large\\times$"}
    #mixer = d.block {x: 300, y: 80, width: 60, height: 50, label: "Mixer"}
    mixer.left.inp {line: 80, label: "$f(t)$", width: 40}
    mixer.top.label
        label: "$f(t) \\cdot p_c(t)$"
        width: 100, center: true
    
    gen = mixer.bottom.to {line: 50, width: 120, height: 80, id: "prn"}
    gen.left.inp {line: 50, label: "Seed", width: 50}
    gen.top.label {label: "$p_c(t)$", width: 50}
    
    int = mixer.right.from 
        line: 60, width: 80, height: 70
        label: "$\\Large\\int_{t-\\frac{1}{R}}^t$"
    int.right.label
        label: "$t = \\frac{n}{R}$"
        width: 70
    int.right.out {line: 90, label: "$y[n]$", width: 50}

#!end (363)

