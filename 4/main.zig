const std = @import("std");

pub fn main() anyerror!void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();

    const allocator = arena.allocator();

    const stdout = std.io.getStdOut().writer();

    var path_buffer: [std.fs.MAX_PATH_BYTES]u8 = undefined;
    const path = try std.fs.realpath("./input.txt", &path_buffer);

    const file = try std.fs.openFileAbsolute(path, .{});
    defer file.close();

    var sum: u32 = 0;

    var buf: [1024]u8 = undefined;

    var cardwinsmap = std.AutoHashMap(u32, std.ArrayList(u32)).init(allocator);
    defer cardwinsmap.deinit();
    defer {
        var iter = cardwinsmap.iterator();
        while (iter.next()) |entry| {
            entry.value_ptr.deinit();
        }
    }

    while (try file.reader().readUntilDelimiterOrEof(&buf, '\n')) |line| {
        var splitCard = std.mem.tokenizeAny(u8, line, ":");
        const cardsubstring = splitCard.next() orelse continue;
        const numbersubstring = splitCard.next() orelse continue;
        var splitNumber = std.mem.tokenizeAny(u8, cardsubstring, " ");
        _ = splitNumber.next();
        const cardnumberstr = splitNumber.next() orelse continue;
        const cardnumber = try std.fmt.parseInt(u32, cardnumberstr, 10);
        var matches: u5 = 0;

        var splitWinningOwn = std.mem.tokenizeAny(u8, numbersubstring, "|");
        const winningsubstring = splitWinningOwn.next() orelse continue;
        const ownsubstring = splitWinningOwn.next() orelse continue;
        var winningnumbersmap = std.AutoHashMap(u32, void).init(allocator);
        defer winningnumbersmap.deinit();
        var splitWinning = std.mem.tokenizeAny(u8, winningsubstring, " ");
        while (splitWinning.next()) |winningnumberstr| {
            const winningnumber = try std.fmt.parseInt(u32, winningnumberstr, 10);
            try winningnumbersmap.put(winningnumber, void{});
        }
        var splitown = std.mem.tokenizeAny(u8, ownsubstring, " ");
        while (splitown.next()) |ownnumberstr| {
            const ownnumber = try std.fmt.parseInt(u32, ownnumberstr, 10);
            if (winningnumbersmap.getKey(ownnumber) != null) {
                matches += 1;
            }
        }
        var cardwinslist = std.ArrayList(u32).init(allocator);
        if (matches > 0) {
            sum += @as(u32, 1) << (matches - 1);
            for (1..(matches + 1)) |i| {
                try cardwinslist.append(cardnumber + @as(u32, @truncate(i)));
            }
        }
        try cardwinsmap.put(cardnumber, cardwinslist);
    }
    var numberOfCards = @as(u32, 0);
    var cardcontainsmap = std.AutoHashMap(u32, u32).init(allocator);
    defer cardcontainsmap.deinit();
    while (cardwinsmap.count() > 0) {
        var iter = cardwinsmap.iterator();
        while (iter.next()) |entry| {
            var canRemove = true;
            var contains = @as(u32, 0);

            for (entry.value_ptr.items) |card| {
                if (cardcontainsmap.contains(card)) {
                    contains += cardcontainsmap.get(card) orelse 0;
                } else {
                    canRemove = false;
                    break;
                }
            }
            if (canRemove) {
                try cardcontainsmap.put(entry.key_ptr.*, contains + 1);
                numberOfCards += contains + 1;
                entry.value_ptr.deinit();
                _ = cardwinsmap.remove(entry.key_ptr.*);
            }
        }
    }
    try stdout.print("Number of cards: {}\n", .{numberOfCards});
    try stdout.print("Sum: {}\n", .{sum});
}
