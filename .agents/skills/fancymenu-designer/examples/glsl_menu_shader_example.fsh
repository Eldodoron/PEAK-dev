#version 150

// FancyMenu v3 GLSL Fragment Shader Example (arcane_nebula.fsh)
// Place in: /config/fancymenu/assets/shaders/arcane_nebula.fsh
// Compatible with GLSL Menu Background, GLSL Shader Element, and GLSL Decoration Overlay.
// Demonstrates live FancyMenu Variable binding via `uniform float fmVarF_menu_energy;`

uniform float fmVarF_menu_energy; // Bound automatically to FancyMenu variable "menu_energy"

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    // Normalize pixel coordinates (from -1 to 1, aspect-corrected)
    vec2 uv = (fragCoord - 0.5 * iResolution.xy) / max(iResolution.y, 1.0);

    // Subtle mouse parallax offset using Shadertoy iMouse or FancyMenu fmMouseGui
    vec2 mouseOffset = (iMouse.xy / max(iResolution.xy, vec2(1.0)) - 0.5) * 0.18;
    uv += mouseOffset;

    // Read live FancyMenu variable (fallback to 1.0 if unset/zero)
    float energy = max(fmVarF_menu_energy, 0.5);
    float t = iTime * 0.35 * energy;

    // Layered domain-warped cosmic waves
    vec2 p = uv * 2.4;
    for (int i = 1; i < 5; i++) {
        float fi = float(i);
        p.x += 0.35 / fi * sin(fi * 2.5 * p.y + t + 0.3 * fi);
        p.y += 0.35 / fi * cos(fi * 2.5 * p.x + t + 0.5 * fi);
    }

    float intensity = 0.5 + 0.5 * sin(p.x + p.y + t);
    float glow = exp(-length(uv) * 1.65);

    // Deep obsidian-violet to arcane cyan palette
    vec3 colBase = vec3(0.05, 0.04, 0.10);
    vec3 colMid  = vec3(0.24, 0.12, 0.48);
    vec3 colHigh = vec3(0.20, 0.78, 0.95);

    vec3 color = mix(colBase, colMid, smoothstep(0.1, 0.8, intensity));
    color = mix(color, colHigh, pow(intensity, 3.0) * glow * min(energy, 2.0));

    // Subtle vignette
    float vignette = smoothstep(1.35, 0.25, length(uv));
    color *= vignette;

    fragColor = vec4(color, 1.0);
}
