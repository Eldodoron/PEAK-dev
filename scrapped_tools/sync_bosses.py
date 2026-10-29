import os

path = os.path.join("minecraft", "kubejs", "server_scripts", "00_tags.js")
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

start_idx = None
end_idx = None
for i, line in enumerate(lines):
    if "// L_Ender's Cataclysm" in line:
        start_idx = i
    if "'undergarden:forgotten_guardian'" in line:
        end_idx = i
        break

if start_idx is not None and end_idx is not None:
    replacement_lines = [
        "        // L_Ender's Cataclysm\n",
        "        'cataclysm:ancient_remnant',\n",
        "        'cataclysm:ender_guardian',\n",
        "        'cataclysm:ender_golem',\n",
        "        'cataclysm:coralssus',\n",
        "        'cataclysm:aptrgangr',\n",
        "        'cataclysm:ignited_revenant',\n",
        "        'cataclysm:ignis',\n",
        "        'cataclysm:the_leviathan',\n",
        "        'cataclysm:netherite_monstrosity',\n",
        "        'cataclysm:the_harbinger',\n",
        "        'cataclysm:maledictus',\n",
        "        'cataclysm:scylla',\n",
        "        // Bosses of Mass Destruction\n",
        "        'bosses_of_mass_destruction:lich',\n",
        "        'bosses_of_mass_destruction:obsidilith',\n",
        "        'bosses_of_mass_destruction:void_blossom',\n",
        "        'bosses_of_mass_destruction:gauntlet',\n",
        "        // Remnant Bosses\n",
        "        'remnant_bosses:armored_grub',\n",
        "        'remnant_bosses:bone_tyrant',\n",
        "        'remnant_bosses:remnant_ossukage',\n",
        "        // Ice and Fire\n",
        "        'iceandfire:fire_dragon',\n",
        "        'iceandfire:ice_dragon',\n",
        "        'iceandfire:lightning_dragon',\n",
        "        'iceandfire:cyclops',\n",
        "        'iceandfire:gorgon',\n",
        "        'iceandfire:hydra',\n",
        "        'iceandfire:dread_lich',\n",
        "        // Alex's Mobs and Caves\n",
        "        'alexsmobs:void_worm',\n",
        "        'alexscaves:luxtructosaurus',\n",
        "        'alexscaves:tremorzilla',\n",
        "        'alexscaves:forsaken',\n",
        "        'alexscaves:hullbreaker',\n",
        "        // Block Factory's Bosses\n",
        "        'block_factorys_bosses:infernal_dragon',\n",
        "        'block_factorys_bosses:yeti',\n",
        "        'block_factorys_bosses:sandworm',\n",
        "        'block_factorys_bosses:underworld_knight',\n",
        "        'block_factorys_bosses:kraken',\n",
        "        // Magic Bosses\n",
        "        'ars_nouveau:wilden_boss',\n",
        "        'irons_spellbooks:dead_king',\n",
        "        'irons_spellbooks:fire_boss',\n",
        "        // Undergarden and Other Modded Bosses\n",
        "        'undergarden:forgotten_guardian',\n",
        "        'friendsandfoes:wildfire',\n",
        "        'draconicevolution:draconic_guardian',\n",
        "        'unusualend:enderblob_queen'\n"
    ]
    lines[start_idx:end_idx + 1] = replacement_lines
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.writelines(lines)
    print("SUCCESS: 00_tags.js updated.")
else:
    print(f"FAILED: start_idx={start_idx}, end_idx={end_idx}")
