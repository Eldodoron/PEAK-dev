// ==========================================
// PEAK STARTUP SCRIPT - YAGM LUMINOUS GRAVES
// Sets maximum light emission for all YAGM gravestones
// ==========================================

BlockEvents.modification(event => {
    event.modify(/yagm:.*grave.*/, block => {
        block.lightEmission = 15;
    });
});
