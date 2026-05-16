// ==========================================
// PEAK EXPERT MODE — SCRIPT 17
// GOBLIN TRADERS DATAPACK INJECTION
// ==========================================

ServerEvents.generateData('peak', 'goblin_trades', event => {
    // Injecting a new Legendary Trade for the Goblin Trader
    // They will occasionally sell an Infinity Fragment for an insane price!
    
    // We add to the legendary.json for the normal goblin trader
    // The format matches the mod's datapack structure
    event.json('goblintraders:goblin_trades/legendary_trades', {
        "replace": false, // We append, not replace the whole file
        "trades": [
            {
                "trade": {
                    "itemA": {
                        "id": "minecraft:emerald_block",
                        "count": {
                            "min": 32,
                            "max": 64
                        }
                    },
                    "itemB": {
                        "id": "minecraft:netherite_block",
                        "count": {
                            "min": 1,
                            "max": 2
                        }
                    },
                    "result": {
                        "id": "kubejs:infinity_fragment",
                        "count": 1
                    },
                    "maxUses": 1,
                    "experience": 500
                },
                "chance": 10
            },
            {
                "trade": {
                    "itemA": {
                        "id": "minecraft:emerald_block",
                        "count": {
                            "min": 10,
                            "max": 20
                        }
                    },
                    "result": {
                        "id": "artifacts:mimic_spawn_egg",
                        "count": 1
                    },
                    "maxUses": 1,
                    "experience": 100
                },
                "chance": 25
            }
        ]
    });

    // Vein Goblin Trader (Nether) Epic Trades
    event.json('goblintraders:goblin_trades/vein_goblin_trader/epic_custom.json', {
        "replace": false,
        "trades": [
            {
                "trade": {
                    "itemA": {
                        "id": "minecraft:gold_block",
                        "count": {
                            "min": 16,
                            "max": 32
                        }
                    },
                    "result": {
                        "id": "kubejs:primordial_dragon_blood",
                        "count": 1
                    },
                    "maxUses": 1,
                    "experience": 250
                },
                "chance": 15
            }
        ]
    });
    
    console.log('[PEAK Expert Mode] Script 17: Goblin Trades injected!');
});
